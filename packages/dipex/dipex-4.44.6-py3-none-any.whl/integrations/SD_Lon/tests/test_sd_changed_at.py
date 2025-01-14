import datetime
import unittest
import uuid
from collections import OrderedDict
from datetime import date
from datetime import timedelta
from unittest.mock import call
from unittest.mock import MagicMock
from unittest.mock import patch

import click
import hypothesis.strategies as st
import pytest
from hypothesis import given
from parameterized import parameterized
from ra_utils.attrdict import attrdict
from ra_utils.generate_uuid import uuid_generator

from sdlon.models import MOBasePerson, ITUserSystem
from sdlon.it_systems import MUTATION_ADD_IT_SYSTEM_TO_EMPLOYEE
from .fixtures import get_employment_fixture
from .fixtures import get_read_employment_changed_fixture
from .fixtures import get_sd_person_fixture
from .fixtures import read_employment_fixture
from sdlon.config import ChangedAtSettings
from sdlon.sd_changed_at import ChangeAtSD
from sdlon.sd_changed_at import get_from_date


@given(test_from_date=st.datetimes())
def test_getfrom_date(test_from_date):
    """Test reading latest date from rundb"""
    with patch(
        "integrations.rundb.db_overview.DBOverview._read_last_line",
        return_value=((test_from_date, "Update ended at ---")),
    ):
        from_date = get_from_date("test", force=False)
        assert from_date == test_from_date


@given(test_from_date=st.datetimes())
def test_getfrom_date_running(test_from_date):
    """Test raising error if last import didn't finish"""
    with patch(
        "integrations.rundb.db_overview.DBOverview._read_last_line",
        return_value=((test_from_date, "Running")),
    ):
        with pytest.raises(click.ClickException):
            get_from_date("test", force=False)


@given(test_from_date=st.datetimes())
@patch("integrations.rundb.db_overview.DBOverview.delete_last_row")
def test_getfrom_date_force(delete_mock, test_from_date):
    """Test reading though last import didn't finish using force=True"""
    with patch(
        "integrations.rundb.db_overview.DBOverview._read_last_line",
        return_value=((test_from_date, "Running")),
    ):
        get_from_date("test", force=True)
        delete_mock.assert_called_once()


class ChangeAtSDTest(ChangeAtSD):
    def __init__(self, *args, **kwargs):
        self.morahelper_mock = MagicMock()
        self.morahelper_mock.read_organisation.return_value = (
            "00000000-0000-0000-0000-000000000000"
        )
        self.primary_types_mock = MagicMock()
        self.primary_engagement_mock = MagicMock()
        self.fix_departments_mock = MagicMock()
        self.mo_graphql_client = MagicMock()

        self._get_job_sync = MagicMock()

        self._create_class = MagicMock()
        self._create_class.return_value = "new_class_uuid"

        super().__init__(*args, **kwargs)

    def _get_primary_types(self, mora_helper):
        return self.primary_types_mock

    def _get_primary_engagement_updater(self):
        return self.primary_engagement_mock

    def _get_fix_departments(self):
        return self.fix_departments_mock

    def _read_forced_uuids(self):
        return {}

    def _get_mora_helper(self, mora_base):
        return self.morahelper_mock


def setup_sd_changed_at(updates=None, hours=24):
    # TODO: remove integrations.SD_Lon.terminate_engagement_with_to_only
    settings_dict = {
        "sd_global_from_date": "1970-01-01",
        "sd_import_run_db": "run_db.sqlite",
        "sd_institution_identifier": "XY",
        "sd_password": "secret",
        "sd_user": "user",
        "sd_job_function": "JobPositionIdentifier",
        "sd_use_ad_integration": False,
        "sd_monthly_hourly_divide": 8000,
        "mora_base": "http://dummy.url",
        "mox_base": "http://dummy.url",
    }
    if updates:
        settings_dict.update(updates)

    settings = ChangedAtSettings.parse_obj(settings_dict)

    today = date.today()
    start_date = today

    sd_updater = ChangeAtSDTest(
        settings, start_date, start_date + timedelta(hours=hours)
    )

    return sd_updater


class Test_sd_changed_at(unittest.TestCase):
    @patch("sdlon.sd_common.sd_lookup_settings")
    @patch("sdlon.sd_common.requests.get")
    def test_get_sd_person(self, requests_get, sd_settings):
        """Test that read_person does the expected transformation."""
        sd_settings.return_value = ("", "", "")

        cpr = "0101709999"
        sd_reply, expected_read_person_result = get_sd_person_fixture(
            cpr=cpr, first_name="John", last_name="Deere", employment_id="01337"
        )

        requests_get.return_value = sd_reply

        sd_updater = setup_sd_changed_at()
        result = sd_updater.get_sd_person(cpr=cpr)
        self.assertEqual(result, expected_read_person_result)

    @patch("sdlon.sd_changed_at.get_employee")
    def test_update_changed_persons(self, mock_get_employee: MagicMock):
        # Arrange
        cpr = "0101709999"
        first_name = "John"
        last_name = "Deere"

        _, read_person_result = get_sd_person_fixture(
            cpr=cpr,
            first_name=first_name,
            last_name=last_name,
            employment_id="01337",
        )

        sd_updater = setup_sd_changed_at()
        sd_updater.get_sd_person = lambda cpr: read_person_result

        generate_uuid = uuid_generator("test")
        org_uuid = str(generate_uuid("org_uuid"))
        user_uuid = str(generate_uuid("user_uuid"))

        sd_updater.org_uuid = org_uuid

        mock_get_employee.return_value = MOBasePerson(
            cpr=cpr,
            uuid=uuid.UUID(user_uuid),
            name=f"Old firstname {last_name}",
            givenname="Old firstname",
            surname=last_name,
        )

        morahelper = sd_updater.morahelper_mock
        _mo_post = morahelper._mo_post
        _mo_post.return_value = attrdict(
            {"status_code": 201, "json": lambda: user_uuid}
        )
        self.assertFalse(_mo_post.called)

        # Act
        sd_updater.update_changed_persons(in_cpr=cpr)

        # Assert
        _mo_post.assert_called_with(
            "e/create",
            {
                "type": "employee",
                "givenname": first_name,
                "surname": last_name,
                "cpr_no": cpr,
                "org": {"uuid": org_uuid},
                "uuid": user_uuid,
                "user_key": user_uuid,
            },
        )

    @patch(
        "sdlon.sd_changed_at.uuid4",
        return_value=uuid.UUID("6b7f5014-faf8-11ed-aa9c-73f93fec45b0"),
    )
    @patch("sdlon.sd_changed_at.get_employee")
    @patch("sdlon.it_systems.date")
    def test_create_sd_to_ad_it_system_for_new_sd_person(
        self, mock_date: MagicMock, mock_get_employee: MagicMock, mock_uuid4: MagicMock
    ):
        """
        This test ensures that the "AD-bruger fra SD" IT-system is created on
        employees in MO for new SD persons if

        1) The environment variable SD_PHONE_NUMBER_ID_FOR_AD_CREATION is true
        2) The SD person has the appropriate string (e.g.) "14"
           in the <TelephoneNumberIdentifier> in their <ContactInformation>
        """
        # Arrange
        mock_date.today = MagicMock(return_value=date(2000, 1, 1))
        sd_updater = setup_sd_changed_at(
            updates={"sd_phone_number_id_for_ad_creation": True}
        )
        sd_updater.get_sd_persons_changed = MagicMock(
            return_value=[
                {
                    "PersonCivilRegistrationIdentifier": "1111111111",
                    "PersonGivenName": "Bruce",
                    "PersonSurnameName": "Lee",
                    "Employment": [
                        {
                            "EmploymentIdentifier": "12345",
                            "ContactInformation": {
                                "TelephoneNumberIdentifier": ["12345678", "14"]
                            },
                        },
                        {
                            "EmploymentIdentifier": "54321",
                            "ContactInformation": {
                                "TelephoneNumberIdentifier": ["87654321", "14"]
                            },
                        },
                    ],
                }
            ]
        )
        mock_execute = MagicMock(
            return_value={
                "itsystems": {
                    "objects": [{"uuid": "988dead8-7564-464a-8339-b7057bfa2665"}]
                }
            }
        )
        sd_updater.mo_graphql_client.execute = mock_execute
        mock_get_employee.return_value = None

        mock_mo_post = MagicMock(
            return_value=attrdict(
                {
                    "status_code": 201,
                    "json": lambda: "6b7f5014-faf8-11ed-aa9c-73f93fec45b0",
                }
            )
        )
        sd_updater.morahelper_mock._mo_post = mock_mo_post

        # Act
        sd_updater.update_changed_persons()

        # Assert
        mock_execute.assert_any_call(
            MUTATION_ADD_IT_SYSTEM_TO_EMPLOYEE,
            variable_values={
                "input": {
                    "user_key": "12345",
                    "itsystem": "988dead8-7564-464a-8339-b7057bfa2665",
                    "validity": {"from": "2000-01-01"},
                    "person": "6b7f5014-faf8-11ed-aa9c-73f93fec45b0",
                }
            },
        )
        mock_execute.assert_any_call(
            MUTATION_ADD_IT_SYSTEM_TO_EMPLOYEE,
            variable_values={
                "input": {
                    "user_key": "54321",
                    "itsystem": "988dead8-7564-464a-8339-b7057bfa2665",
                    "validity": {"from": "2000-01-01"},
                    "person": "6b7f5014-faf8-11ed-aa9c-73f93fec45b0",
                }
            },
        )

    @patch(
        "sdlon.sd_changed_at.uuid4",
        return_value=uuid.UUID("6b7f5014-faf8-11ed-aa9c-73f93fec45b0"),
    )
    @patch("sdlon.sd_changed_at.get_employee")
    @patch("sdlon.it_systems.date")
    def test_do_not_create_sd_to_ad_it_system_for_new_sd_person(
        self, mock_date: MagicMock, mock_get_employee: MagicMock, mock_uuid4: MagicMock
    ):
        """
        This test ensures that we do NOT create the "AD-bruger fra SD" IT-system
        on employees in MO for new SD persons if

        1) The environment variable SD_PHONE_NUMBER_ID_FOR_AD_CREATION is true
        2) The SD person has does NOT have the appropriate string (e.g.)
           "14" in the <TelephoneNumberIdentifier> in their
           <ContactInformation>
        """

        # Arrange
        mock_date.today = MagicMock(return_value=date(2000, 1, 1))
        sd_updater = setup_sd_changed_at(
            updates={"sd_phone_number_id_for_ad_creation": True}
        )
        sd_updater.get_sd_persons_changed = MagicMock(
            return_value=[
                {
                    "PersonCivilRegistrationIdentifier": "1111111111",
                    "PersonGivenName": "Bruce",
                    "PersonSurnameName": "Lee",
                    "ContactInformation": {"TelephoneNumberIdentifier": ["12345678"]},
                    "Employment": {"EmploymentIdentifier": "12345"},
                }
            ]
        )
        mock_execute = MagicMock(
            return_value={
                "itsystems": {
                    "objects": [{"uuid": "988dead8-7564-464a-8339-b7057bfa2665"}]
                }
            }
        )
        sd_updater.mo_graphql_client.execute = mock_execute
        mock_get_employee.return_value = None

        mock_mo_post = MagicMock(
            return_value=attrdict(
                {
                    "status_code": 201,
                    "json": lambda: "6b7f5014-faf8-11ed-aa9c-73f93fec45b0",
                }
            )
        )
        sd_updater.morahelper_mock._mo_post = mock_mo_post

        # Act
        sd_updater.update_changed_persons()

        # Assert
        mock_execute.assert_not_called()

    @patch(
        "sdlon.sd_changed_at.get_sd_to_ad_it_system_uuid",
        return_value=uuid.UUID("988dead8-7564-464a-8339-b7057bfa2665"),
    )
    @patch("sdlon.sd_changed_at.get_employee_it_systems", return_value=[])
    @patch("sdlon.sd_changed_at.get_employee")
    @patch("sdlon.it_systems.date")
    def test_create_sd_to_ad_it_system_for_existing_mo_person(
        self,
        mock_date: MagicMock,
        mock_get_employee: MagicMock,
        mock_get_employee_it_systems: MagicMock,
        mock_get_sd_to_ad_it_system_uuid: MagicMock,
    ):
        """
        This test ensures that the "AD-bruger fra SD" IT-system is created on
        employees in MO for SD persons already existing in MO if

        1) The environment variable SD_PHONE_NUMBER_ID_FOR_AD_CREATION is true
        2) The SD person has the appropriate string (e.g.) "14"
           in the <TelephoneNumberIdentifier> in their <ContactInformation>

           and

           The IT-system does not already exist for the employee
        """

        # Arrange
        mock_date.today = MagicMock(return_value=date(2000, 1, 1))
        sd_updater = setup_sd_changed_at(
            updates={"sd_phone_number_id_for_ad_creation": True}
        )
        sd_updater.get_sd_persons_changed = MagicMock(
            return_value=[
                {
                    "PersonCivilRegistrationIdentifier": "1111111111",
                    "PersonGivenName": "Bruce",
                    "PersonSurnameName": "Lee",
                    "Employment": {
                        "EmploymentIdentifier": "12345",
                        "ContactInformation": {
                            "TelephoneNumberIdentifier": ["12345678", "14"]
                        },
                    },
                }
            ]
        )
        mock_execute = MagicMock()
        sd_updater.mo_graphql_client.execute = mock_execute
        mock_get_employee.return_value = MOBasePerson(
            cpr="1111111111",
            givenname="Bruce",
            surname="Lee",
            name="Bruce Lee",
            uuid=uuid.UUID("6b7f5014-faf8-11ed-aa9c-73f93fec45b0"),
        )

        # Act
        sd_updater.update_changed_persons()

        # Assert
        mock_execute.assert_called_with(
            MUTATION_ADD_IT_SYSTEM_TO_EMPLOYEE,
            variable_values={
                "input": {
                    "user_key": "12345",
                    "itsystem": "988dead8-7564-464a-8339-b7057bfa2665",
                    "validity": {"from": "2000-01-01"},
                    "person": "6b7f5014-faf8-11ed-aa9c-73f93fec45b0",
                }
            },
        )

    @parameterized.expand(
        [
            (
                ["12345678", "14"],
                [
                    ITUserSystem(
                        uuid=uuid.UUID("988dead8-7564-464a-8339-b7057bfa2665"),
                        user_key="12345",
                    )
                ],
            ),
            (["12345678"], []),
        ]
    )
    @patch(
        "sdlon.sd_changed_at.get_sd_to_ad_it_system_uuid",
        return_value=uuid.UUID("988dead8-7564-464a-8339-b7057bfa2665"),
    )
    @patch("sdlon.sd_changed_at.get_employee_it_systems")
    @patch("sdlon.sd_changed_at.get_employee")
    @patch("sdlon.it_systems.date")
    def test_do_not_create_sd_to_ad_it_system_for_existing_user(
        self,
        telephone_number_ids: list[str],
        employee_it_systems: list[uuid.UUID],
        mock_date: MagicMock,
        mock_get_employee: MagicMock,
        mock_get_employee_it_systems: MagicMock,
        mock_get_sd_to_ad_it_system_uuid: MagicMock,
    ):
        """
        This test ensures that we do NOT create the "AD-bruger fra SD" IT-system
        on employees in MO for SD persons already existing in MO if

        1) The environment variable SD_PHONE_NUMBER_ID_FOR_AD_CREATION is true

        and

        2) The SD person has does NOT have the appropriate string (e.g.)
           "14" in the <TelephoneNumberIdentifier> in their
           <ContactInformation>

            or

            The IT-system is already exists for the employee.
        """

        # Arrange
        mock_date.today = MagicMock(return_value=date(2000, 1, 1))
        sd_updater = setup_sd_changed_at(
            updates={"sd_phone_number_id_for_ad_creation": True}
        )
        mock_get_employee_it_systems.return_value = employee_it_systems
        sd_updater.get_sd_persons_changed = MagicMock(
            return_value=[
                {
                    "PersonCivilRegistrationIdentifier": "1111111111",
                    "PersonGivenName": "Bruce",
                    "PersonSurnameName": "Lee",
                    "Employment": {
                        "EmploymentIdentifier": "12345",
                        "ContactInformation": {
                            "TelephoneNumberIdentifier": telephone_number_ids
                        },
                    },
                }
            ]
        )
        mock_execute = MagicMock()
        sd_updater.mo_graphql_client.execute = mock_execute
        mock_get_employee.return_value = MOBasePerson(
            cpr="1111111111",
            givenname="Bruce",
            surname="Lee",
            name="Bruce Lee",
            uuid=uuid.UUID("6b7f5014-faf8-11ed-aa9c-73f93fec45b0"),
        )

        # Act
        sd_updater.update_changed_persons()

        # Assert
        mock_execute.assert_not_called()

    @given(status=st.sampled_from(["1", "S"]))
    @patch("sdlon.sd_common.sd_lookup_settings")
    @patch("sdlon.sd_common.requests.get")
    def test_read_employment_changed(
        self,
        requests_get,
        sd_settings,
        status,
    ):
        sd_settings.return_value = ("", "", "")

        sd_reply, expected_read_employment_result = read_employment_fixture(
            cpr="0101709999",
            employment_id="01337",
            job_id="1234",
            job_title="EDB-Mand",
            status=status,
        )

        requests_get.return_value = sd_reply
        sd_updater = setup_sd_changed_at()
        result = sd_updater.read_employment_changed()
        self.assertEqual(result, expected_read_employment_result)

    def test_do_not_create_engagement_for_inconsistent_external_emp(self):
        """
        We are testing bullet 4 in
        https://os2web.atlassian.net/browse/MO-245, i.e. that we do not
        create a MO engagement for a newly created external SD employee
        who (unintentionally) has a JobPositionIdentifier below
        no_salary_minimum.

        NOTE: an external SD employee has an EmploymentIdentifier containing
        letters (at least in some municipalities)
        """

        sd_updater = setup_sd_changed_at(
            {
                "sd_no_salary_minimum_id": 9000,
            }
        )
        sd_updater.read_employment_changed = (
            lambda: get_read_employment_changed_fixture(
                employment_id="ABCDE", job_pos_id=8000  # See doc-string above
            )
        )

        morahelper = sd_updater.morahelper_mock
        morahelper.read_user.return_value.__getitem__.return_value = "user_uuid"

        sd_updater.create_new_engagement = MagicMock()

        # Act
        sd_updater.update_all_employments()

        # Assert
        sd_updater.create_new_engagement.assert_not_called()

    @given(status=st.sampled_from(["1", "S"]))
    def test_update_all_employments(self, status):

        cpr = "0101709999"
        employment_id = "01337"

        _, read_employment_result = read_employment_fixture(
            cpr=cpr,
            employment_id=employment_id,
            job_id="1234",
            job_title="EDB-Mand",
            status=status,
        )

        sd_updater = setup_sd_changed_at()
        sd_updater.read_employment_changed = lambda: read_employment_result

        morahelper = sd_updater.morahelper_mock
        morahelper.read_user.return_value.__getitem__.return_value = "user_uuid"

        if status == "1":  # Creates call create engagement, if no eng exists
            sd_updater.create_new_engagement = MagicMock()

            engagement = read_employment_result[0]["Employment"]
            # First employment status entry from read_employment_result
            status = read_employment_result[0]["Employment"]["EmploymentStatus"][0]

            self.assertFalse(sd_updater.create_new_engagement.called)
            sd_updater.update_all_employments()
            sd_updater.create_new_engagement.assert_called_with(
                engagement, status, cpr, "user_uuid"
            )
        elif status == "S":  # Deletes call terminante engagement
            morahelper.read_user_engagement.return_value = [{"user_key": employment_id}]
            sd_updater._terminate_engagement = MagicMock()

            status = read_employment_result[0]["Employment"]["EmploymentStatus"]

            self.assertFalse(sd_updater._terminate_engagement.called)
            sd_updater.update_all_employments()
            sd_updater._terminate_engagement.assert_called_with(
                user_key=employment_id,
                person_uuid="user_uuid",
                from_date=status["ActivationDate"],
            )

    @parameterized.expand(
        [
            ["07777", "monthly pay"],
            ["90000", "hourly pay"],
            ["C3-P0", "employment pay"],
        ]
    )
    def test_create_new_engagement(self, employment_id, engagement_type):

        cpr = "0101709999"
        job_id = "1234"

        _, read_employment_result = read_employment_fixture(
            cpr=cpr,
            employment_id=employment_id,
            job_id=job_id,
            job_title="EDB-Mand",
        )

        sd_updater = setup_sd_changed_at()

        sd_updater.engagement_types = {
            "månedsløn": "monthly pay",
            "timeløn": "hourly pay",
            "engagement_type" + job_id: "employment pay",
        }

        morahelper = sd_updater.morahelper_mock

        # Load noop NY logic
        sd_updater.apply_NY_logic = (
            lambda org_unit, user_key, validity, person_uuid: org_unit
        )
        # Set primary types
        sd_updater.primary_types = {
            "primary": "primary_uuid",
            "non_primary": "non_primary_uuid",
            "no_salary": "no_salary_uuid",
            "fixed_primary": "fixed_primary_uuid",
        }

        engagement = read_employment_result[0]["Employment"]
        # First employment status entry from read_employment_result
        status = read_employment_result[0]["Employment"]["EmploymentStatus"][0]

        _mo_post = morahelper._mo_post
        _mo_post.return_value = attrdict(
            {
                "status_code": 201,
            }
        )
        self.assertFalse(_mo_post.called)

        sd_updater._create_engagement_type = MagicMock()
        sd_updater._create_engagement_type.return_value = "new_engagement_type_uuid"

        sd_updater._create_professions = MagicMock()
        sd_updater._create_professions.return_value = "new_profession_uuid"

        sd_updater.create_new_engagement(engagement, status, cpr, "user_uuid")
        _mo_post.assert_called_with(
            "details/create",
            {
                "type": "engagement",
                "org_unit": {"uuid": "department_uuid"},
                "person": {"uuid": "user_uuid"},
                "job_function": {"uuid": "new_profession_uuid"},
                "primary": {"uuid": "non_primary_uuid"},
                "engagement_type": {"uuid": engagement_type},
                "user_key": employment_id,
                "fraction": 0,
                "validity": {"from": "2020-11-10", "to": "2021-02-09"},
            },
        )
        sd_updater._create_engagement_type.assert_not_called()
        sd_updater._create_professions.assert_called_once()

    def test_terminate_engagement(self):

        employment_id = "01337"

        sd_updater = setup_sd_changed_at()
        morahelper = sd_updater.morahelper_mock

        sd_updater.mo_engagements_cache["user_uuid"] = [
            {
                "user_key": employment_id,
                "uuid": "mo_engagement_uuid",
            }
        ]

        _mo_post = morahelper._mo_post
        _mo_post.return_value = attrdict(
            {"status_code": 200, "text": lambda: "mo_engagement_uuid"}
        )
        self.assertFalse(_mo_post.called)
        sd_updater._terminate_engagement(
            user_key=employment_id, person_uuid="user_uuid", from_date="2020-11-01"
        )
        _mo_post.assert_called_once_with(
            "details/terminate",
            {
                "type": "engagement",
                "uuid": "mo_engagement_uuid",
                "validity": {"from": "2020-11-01", "to": None},
            },
        )

    def test_terminate_engagement_returns_false_when_no_mo_engagement(self):
        sd_updater = setup_sd_changed_at()

        morahelper = sd_updater.morahelper_mock
        mock_read_user_engagement = morahelper.read_user_engagement
        mock_read_user_engagement.return_value = []

        self.assertFalse(
            sd_updater._terminate_engagement(
                user_key="12345", person_uuid=str(uuid.uuid4()), from_date="2021-10-05"
            )
        )

    def test_terminate_engagement_when_to_date_set(self):
        sd_updater = setup_sd_changed_at()
        sd_updater.mo_engagements_cache["person_uuid"] = [
            {
                "user_key": "00000",
                "uuid": "mo_engagement_uuid",
            }
        ]

        morahelper = sd_updater.morahelper_mock
        mock_post_mo = morahelper._mo_post
        mock_post_mo.return_value = attrdict(
            {"status_code": 200, "text": lambda: "mo_engagement_uuid"}
        )

        sd_updater._terminate_engagement(
            user_key="00000",
            person_uuid="person_uuid",
            from_date="2021-10-15",
            to_date="2021-10-20",
        )
        mock_post_mo.assert_called_once_with(
            "details/terminate",
            {
                "type": "engagement",
                "uuid": "mo_engagement_uuid",
                "validity": {"from": "2021-10-15", "to": "2021-10-20"},
            },
        )

    @unittest.skip("Will be finished when fix is deployed...")
    def test_skip_sd_employments_in_skip_list(self):
        """
        Test that SD employments with JobPositionIdentifiers in the skip list
        provided in the setting "sd_skip_employment_types" are actually skipped.
        """

        # Arrange
        sd_updater = setup_sd_changed_at(
            updates={"sd_skip_employment_types": ["1", "2", "3"]}
        )

        # _, read_employment_result = read_employment_fixture(
        #     cpr="1234569999",
        #     employment_id="12345",
        #     job_id="2",  # Found in the skip list
        #     job_title="Kung Fu Fighter",
        # )
        # from pprint import pprint
        # pprint(read_employment_result)
        sd_updater.read_employment_changed = lambda: [
            OrderedDict(
                {
                    "PersonCivilRegistrationIdentifier": "1212129999",
                    "Employment": {
                        "EmploymentIdentifier": "12345",
                        "EmploymentDate": "2020-11-10",
                        "AnniversaryDate": "2004-08-15",
                        "EmploymentDepartment": {
                            "ActivationDate": "2020-11-10",
                            "DeactivationDate": "9999-12-31",
                            "DepartmentIdentifier": "department_id",
                            "DepartmentUUIDIdentifier": str(uuid.uuid4()),
                        },
                        "Profession": [
                            {
                                "ActivationDate": "2020-11-10",
                                "DeactivationDate": "2021-12-31",
                                "JobPositionIdentifier": "2",
                                "EmploymentName": "Skip this employment",
                                "AppointmentCode": "0",
                            },
                            {
                                "ActivationDate": "2022-01-01",
                                "DeactivationDate": "9999-12-31",
                                "JobPositionIdentifier": "4",
                                "EmploymentName": "Kung Fu Fighter",
                                "AppointmentCode": "0",
                            },
                        ],
                        "EmploymentStatus": {
                            "ActivationDate": "2020-11-10",
                            "DeactivationDate": "9999-12-31",
                            "EmploymentStatusCode": "1",
                        },
                    },
                }
            )
        ]

        morahelper = sd_updater.morahelper_mock
        morahelper.read_user.return_value.__getitem__.return_value = "user_uuid"

        sd_updater.create_new_engagement = MagicMock()
        sd_updater.edit_engagement = MagicMock()
        sd_updater._terminate_engagement = MagicMock()

        # Act
        sd_updater.update_all_employments()

        # Assert

        # Since the SD employment has a JobPositionIdentifier in the skip list,
        # we must ensure that engagements are not created or modified
        sd_updater.create_new_engagement.assert_not_called()
        sd_updater.edit_engagement.assert_not_called()
        sd_updater._terminate_engagement.assert_not_called()

    @parameterized.expand([("2021-10-15", "2021-10-15"), ("9999-12-31", None)])
    def test_handle_status_changes_terminates_let_go_employment_status(
        self, sd_deactivation_date, mo_termination_to_date
    ):
        cpr = "0101709999"
        employment_id = "01337"

        _, read_employment_result = read_employment_fixture(
            cpr=cpr,
            employment_id=employment_id,
            job_id="1234",
            job_title="EDB-Mand",
            status="1",
        )
        sd_employment = read_employment_result[0]["Employment"]
        sd_employment["EmploymentStatus"].pop(0)  # Remove the one with status 8
        sd_employment["EmploymentStatus"][0]["DeactivationDate"] = sd_deactivation_date

        sd_updater = setup_sd_changed_at()
        sd_updater.mo_engagements_cache["person_uuid"] = [
            {
                "user_key": employment_id,
                "uuid": "mo_engagement_uuid",
            }
        ]

        morahelper = sd_updater.morahelper_mock
        mock_mo_post = morahelper._mo_post
        mock_mo_post.return_value = attrdict(
            {"status_code": 200, "text": lambda: "mo_engagement_uuid"}
        )

        sd_updater._handle_employment_status_changes(
            cpr=cpr, sd_employment=sd_employment, person_uuid="person_uuid"
        )

        mock_mo_post.assert_called_once_with(
            "details/terminate",
            {
                "type": "engagement",
                "uuid": "mo_engagement_uuid",
                "validity": {"from": "2021-02-10", "to": mo_termination_to_date},
            },
        )

    def test_handle_status_changes_terminates_slettet_employment_status(self):
        cpr = "0101709999"
        employment_id = "01337"

        _, read_employment_result = read_employment_fixture(
            cpr=cpr,
            employment_id=employment_id,
            job_id="1234",
            job_title="EDB-Mand",
            status="S",
        )
        sd_employment = read_employment_result[0]["Employment"]

        sd_updater = setup_sd_changed_at()
        sd_updater.mo_engagements_cache["person_uuid"] = [
            {
                "user_key": employment_id,
                "uuid": "mo_engagement_uuid",
            }
        ]

        morahelper = sd_updater.morahelper_mock
        mock_mo_post = morahelper._mo_post
        mock_mo_post.return_value = attrdict(
            {"status_code": 200, "text": lambda: "mo_engagement_uuid"}
        )

        sd_updater._handle_employment_status_changes(
            cpr=cpr, sd_employment=sd_employment, person_uuid="person_uuid"
        )

        mock_mo_post.assert_called_once_with(
            "details/terminate",
            {
                "type": "engagement",
                "uuid": "mo_engagement_uuid",
                "validity": {"from": "2020-11-01", "to": None},
            },
        )

    @parameterized.expand(
        [
            ["07777", "monthly pay"],
            ["90000", "hourly pay"],
            ["C3-P0", "employment pay"],
        ]
    )
    def test_update_all_employments_editing(self, employment_id, engagement_type):

        cpr = "0101709999"
        job_id = "1234"

        _, read_employment_result = read_employment_fixture(
            cpr=cpr,
            employment_id=employment_id,
            job_id=job_id,
            job_title="EDB-Mand",
        )

        sd_updater = setup_sd_changed_at()
        sd_updater.engagement_types = {
            "månedsløn": "monthly pay",
            "timeløn": "hourly pay",
            "engagement_type" + job_id: "employment pay",
        }

        sd_updater.read_employment_changed = lambda: read_employment_result
        # Load noop NY logic
        sd_updater.apply_NY_logic = (
            lambda org_unit, user_key, validity, person_uuid: org_unit
        )

        morahelper = sd_updater.morahelper_mock
        morahelper.read_user.return_value.__getitem__.return_value = "user_uuid"
        morahelper.read_user_engagement.return_value = [
            {
                "user_key": employment_id,
                "uuid": "mo_engagement_uuid",
                "validity": {"to": "9999-12-31"},
            }
        ]

        # Set primary types
        sd_updater.primary_types = {
            "primary": "primary_uuid",
            "non_primary": "non_primary_uuid",
            "no_salary": "no_salary_uuid",
            "fixed_primary": "fixed_primary_uuid",
        }

        _mo_post = morahelper._mo_post
        _mo_post.return_value = attrdict({"status_code": 201, "text": lambda: "OK"})
        self.assertFalse(_mo_post.called)

        sd_updater._create_engagement_type = MagicMock()
        sd_updater._create_engagement_type.return_value = "new_engagement_type_uuid"

        sd_updater._create_professions = MagicMock()
        sd_updater._create_professions.return_value = "new_profession_uuid"

        sd_updater.update_all_employments()
        # We expect the exact following 4 calls to have been made
        self.assertEqual(len(_mo_post.mock_calls), 5)
        _mo_post.assert_has_calls(
            [
                call(
                    "details/edit",
                    {
                        "type": "engagement",
                        "uuid": "mo_engagement_uuid",
                        "data": {
                            "validity": {"from": "2020-11-10", "to": "2021-02-09"},
                            "primary": {"uuid": "non_primary_uuid"},
                        },
                    },
                ),
                call(
                    "details/edit",
                    {
                        "type": "engagement",
                        "uuid": "mo_engagement_uuid",
                        "data": {
                            "org_unit": {"uuid": "department_uuid"},
                            "validity": {"from": "2020-11-10", "to": None},
                        },
                    },
                ),
                call(
                    "details/edit",
                    {
                        "type": "engagement",
                        "uuid": "mo_engagement_uuid",
                        "data": {
                            "job_function": {"uuid": "new_profession_uuid"},
                            "validity": {"from": "2020-11-10", "to": None},
                        },
                    },
                ),
                call(
                    "details/edit",
                    {
                        "type": "engagement",
                        "uuid": "mo_engagement_uuid",
                        "data": {
                            "engagement_type": {"uuid": engagement_type},
                            "validity": {"from": "2020-11-10", "to": None},
                        },
                    },
                ),
                call(
                    "details/terminate",
                    {
                        "type": "engagement",
                        "uuid": "mo_engagement_uuid",
                        "validity": {"from": "2021-02-10", "to": None},
                    },
                ),
            ]
        )
        sd_updater._create_engagement_type.assert_not_called()
        sd_updater._create_professions.assert_called_once()

    @given(job_position=st.integers(), no_salary_minimum=st.integers())
    @patch("sdlon.sd_changed_at.sd_payloads", autospec=True)
    def test_construct_object(self, sd_payloads_mock, job_position, no_salary_minimum):
        expected = no_salary_minimum is not None
        expected = expected and job_position < no_salary_minimum
        expected = not expected

        sd_updater = setup_sd_changed_at(
            {
                "sd_no_salary_minimum_id": no_salary_minimum,
            }
        )
        sd_updater.apply_NY_logic = (
            lambda org_unit, user_key, validity, person_uuid: org_unit
        )

        morahelper = sd_updater.morahelper_mock
        morahelper.read_ou.return_value = {
            "org_unit_level": {
                "user_key": "IHaveNoIdea",
            },
            "uuid": "uuid-a",
        }
        _mo_post = morahelper._mo_post
        _mo_post.return_value = attrdict({"status_code": 201, "text": lambda: "OK"})

        engagement = {
            "EmploymentIdentifier": "BIGAL",
            "EmploymentDepartment": [{"DepartmentUUIDIdentifier": "uuid-c"}],
            "Profession": [{"JobPositionIdentifier": str(job_position)}],
        }
        status = {
            "ActivationDate": "",
            "DeactivationDate": "",
            "EmploymentStatusCode": "",
        }
        cpr = ""
        result = sd_updater.create_new_engagement(engagement, status, cpr, "uuid-b")
        self.assertEqual(result, expected)
        if expected:
            sd_payloads_mock.create_engagement.assert_called_once()
        else:
            sd_payloads_mock.create_engagement.assert_not_called()

    @given(job_id=st.integers(min_value=0), engagement_exists=st.booleans())
    def test_fetch_engagement_type(self, job_id, engagement_exists):
        """Test that fetch_engagement_type only calls create when class is missing.

        This is done by creating the class if engagement_exists is set.
        I assume this works the same for _fetch_professions as they are similar.
        """
        sd_updater = setup_sd_changed_at()
        sd_updater.engagement_types = {
            "månedsløn": "monthly pay",
            "timeløn": "hourly pay",
        }

        self.assertEqual(len(sd_updater.engagement_types), 2)
        if engagement_exists:
            sd_updater.engagement_types[
                "engagement_type" + str(job_id)
            ] = "old_engagement_type_uuid"
            self.assertEqual(len(sd_updater.engagement_types), 3)
        else:
            self.assertEqual(len(sd_updater.engagement_types), 2)

        engagement_type_uuid = sd_updater._fetch_engagement_type(str(job_id))

        if engagement_exists:
            self.assertEqual(len(sd_updater.engagement_types), 3)
            sd_updater._create_class.assert_not_called()
            self.assertEqual(engagement_type_uuid, "old_engagement_type_uuid")
        else:
            self.assertEqual(len(sd_updater.engagement_types), 3)
            sd_updater._create_class.assert_called_once()
            sd_updater.job_sync.sync_from_sd.assert_called_once()
            self.assertIn("engagement_type" + str(job_id), sd_updater.engagement_types)
            self.assertEqual(engagement_type_uuid, "new_class_uuid")

    def test_edit_engagement(self):
        engagement = OrderedDict(
            [
                ("EmploymentIdentifier", "DEERE"),
                (
                    "Profession",
                    OrderedDict(
                        [
                            ("@changedAtDate", "1970-01-01"),
                            ("ActivationDate", "1960-01-01"),
                            ("DeactivationDate", "9999-12-31"),
                            ("JobPositionIdentifier", "9002"),
                            ("EmploymentName", "dummy"),
                            ("AppointmentCode", "0"),
                        ]
                    ),
                ),
            ]
        )

        sd_updater = setup_sd_changed_at()
        sd_updater.engagement_types = {
            "månedsløn": "monthly pay",
            "timeløn": "hourly pay",
        }
        sd_updater.mo_engagements_cache["person_uuid"] = [
            {
                "user_key": engagement["EmploymentIdentifier"],
                "uuid": "mo_engagement_uuid",
                "validity": {"from": "1950-01-01", "to": None},
            }
        ]

        morahelper = sd_updater.morahelper_mock
        _mo_post = morahelper._mo_post
        _mo_post.return_value = attrdict(
            {
                "status_code": 201,
            }
        )
        sd_updater._create_engagement_type = MagicMock(
            wraps=sd_updater._create_engagement_type
        )
        sd_updater._create_professions = MagicMock(wraps=sd_updater._create_professions)
        # Return 1 on first call, 2 on second call
        sd_updater._create_class.side_effect = [
            "new_class_1_uuid",
            "new_class_2_uuid",
        ]

        sd_updater.edit_engagement(engagement, "person_uuid")

        # Check that the create functions are both called
        sd_updater._create_engagement_type.assert_called_with(
            "engagement_type9002", "9002"
        )
        sd_updater._create_professions.assert_called_with("9002", "9002")
        # And thus that job_sync is called once from each
        sd_updater.job_sync.sync_from_sd.assert_has_calls(
            [call("9002", refresh=True), call("9002", refresh=True)]
        )
        # And that the results are returned to MO
        _mo_post.assert_has_calls(
            [
                call(
                    "details/edit",
                    {
                        "type": "engagement",
                        "uuid": "mo_engagement_uuid",
                        "data": {
                            "job_function": {"uuid": "new_class_1_uuid"},
                            "validity": {"from": "1960-01-01", "to": None},
                        },
                    },
                ),
                call(
                    "details/edit",
                    {
                        "type": "engagement",
                        "uuid": "mo_engagement_uuid",
                        "data": {
                            "engagement_type": {"uuid": "new_class_2_uuid"},
                            "validity": {"from": "1960-01-01", "to": None},
                        },
                    },
                ),
            ]
        )

    @patch("sdlon.sd_common.sd_lookup_settings")
    @patch("sdlon.sd_common.sd_lookup")
    def test_edit_engagement_job_position_id_set_to_value_above_9000(
        self, mock_sd_lookup, mock_sd_lookup_settings
    ):
        """
        If an employment exists in MO but with no engagement (e.g. which happens
        when the MO employment was created with an SD payload having a
        JobPositionIdentifier < 9000) and we receive an SD change payload, where
        the JobPositionIdentifier is set to a value greater than 9000, then we
        must ensure that an engagement is create for the corresponding employee
        in MO.
        """

        # Arrange

        sd_updater = setup_sd_changed_at(
            {
                "sd_monthly_hourly_divide": 80000,
                "sd_no_salary_minimum_id": 9000,
                "sd_import_too_deep": [
                    "Afdelings-niveau",
                    "NY1-niveau",
                ],
            }
        )

        sd_updater.engagement_types = {
            "månedsløn": "monthly pay",
            "timeløn": "hourly pay",
        }

        engagement = OrderedDict(
            [
                ("EmploymentIdentifier", "DEERE"),
                (
                    "Profession",
                    OrderedDict(
                        [
                            ("@changedAtDate", "2021-12-20"),
                            ("ActivationDate", "2021-12-19"),
                            ("DeactivationDate", "9999-12-31"),
                            ("JobPositionIdentifier", "9002"),
                            ("EmploymentName", "dummy"),
                            ("AppointmentCode", "0"),
                        ]
                    ),
                ),
            ]
        )
        mock_sd_lookup_settings.return_value = ("", "", "")

        # Necessary for the _find_engagement call in edit_engagement
        # Mock the call to arrange that no engagements are found for the user
        mora_helper = sd_updater.morahelper_mock
        _mo_lookup = mora_helper._mo_lookup
        _mo_lookup.return_value = []

        # Mock the call in sd_updater.read_employment_at(...)
        mock_sd_lookup.return_value = get_employment_fixture(
            1234561234, "emp_id", "dep_id", "dep_uuid", "9002", "job_title"
        )

        mock_apply_NY_logic = MagicMock()
        sd_updater.apply_NY_logic = mock_apply_NY_logic
        mock_apply_NY_logic.return_value = "org_unit_uuid"

        primary_types = sd_updater.primary_types_mock
        __getitem__ = primary_types.__getitem__
        __getitem__.return_value = "primary_uuid"

        _mo_post = mora_helper._mo_post
        _mo_post.return_value = attrdict(
            {
                "status_code": 201,
            }
        )

        # Act

        sd_updater.edit_engagement(engagement, "person_uuid")

        # Assert

        _mo_post.assert_called_once_with(
            "details/create",
            {
                "engagement_type": {"uuid": "new_class_uuid"},
                "fraction": 0,
                "job_function": {"uuid": "new_class_uuid"},
                "org_unit": {"uuid": "org_unit_uuid"},
                "person": {"uuid": "person_uuid"},
                "primary": {"uuid": "primary_uuid"},
                "type": "engagement",
                "user_key": "emp_id",
                "validity": {"from": "2020-11-10", "to": "2021-02-09"},
            },
        )

    @patch("sdlon.sd_common.sd_lookup_settings")
    def test_edit_engagement_profession_job_position_id_set_to_value_below_9000(
        self, mock_sd_lookup_settings
    ):
        """
        If an employment exists in MO WITH an engagement and we receive an
        SD change payload, where the JobPositionIdentifier is set to a value
        less than 9000, then we must ensure that an engagement is terminated
        for the corresponding employee in MO.
        """

        # Arrange

        sd_updater = setup_sd_changed_at(
            {
                "sd_monthly_hourly_divide": 80000,
                "sd_no_salary_minimum_id": 9000,
                "sd_import_too_deep": [
                    "Afdelings-niveau",
                    "NY1-niveau",
                ],
            }
        )

        engagement = OrderedDict(
            [
                ("EmploymentIdentifier", "DEERE"),
                (
                    "Profession",
                    OrderedDict(
                        [
                            ("@changedAtDate", "2021-12-20"),
                            ("ActivationDate", "2021-12-19"),
                            ("DeactivationDate", "9999-12-31"),
                            ("JobPositionIdentifier", "8000"),
                            ("EmploymentName", "dummy"),
                            ("AppointmentCode", "0"),
                        ]
                    ),
                ),
            ]
        )

        mo_eng = {"user_key": "12345", "person": {"uuid": "person_uuid"}}

        mock_sd_lookup_settings.return_value = ("", "", "")

        # Mock the terminate engagement call
        mock_terminate_engagement = MagicMock()
        sd_updater._terminate_engagement = mock_terminate_engagement
        mock_terminate_engagement.return_value = True

        # Act

        sd_updater.edit_engagement_profession(engagement, mo_eng)

        # Assert

        mock_terminate_engagement.assert_called_once_with(
            "12345", "person_uuid", "2021-12-19", None
        )

    @patch("sdlon.sd_changed_at.update_existing_engagement")
    def test_edit_engagement_handles_empty_professions_list(self, mock_update):
        """Handle an empty `professions` list in the engagement returned by SD"""
        # This is a regression test for #47799

        # Arrange
        sd_updater = setup_sd_changed_at()
        sd_updater._find_engagement = lambda *args: ["mo-eng"]
        engagement = OrderedDict(
            [
                ("EmploymentIdentifier", "DEERE"),
                ("Profession", []),
            ]
        )

        # Act
        sd_updater.edit_engagement(engagement, "person_uuid")

        # Assert
        mock_update.assert_called_once()

    def test_do_not_edit_profession_when_sd_overwrite_emp_name_set(self):
        # Arrange
        sd_updater = setup_sd_changed_at(
            updates={
                "sd_job_function": "EmploymentName",
                "sd_overwrite_existing_employment_name": False,
            }
        )

        sd_updater._find_engagement = lambda *args: ["mo-eng"]
        engagement = OrderedDict(
            [
                ("EmploymentIdentifier", "12345"),
                (
                    "Profession",
                    [
                        ("@changedAtDate", "2021-12-20"),
                        ("ActivationDate", "2021-12-19"),
                        ("DeactivationDate", "9999-12-31"),
                        ("JobPositionIdentifier", "8000"),
                        ("EmploymentName", "ThisNewValueShouldNotBeWrittenToMO"),
                        ("AppointmentCode", "0"),
                    ],
                ),
            ]
        )

        sd_updater.edit_engagement_profession = MagicMock()
        sd_updater.edit_engagement_type = MagicMock()

        # Act
        sd_updater.edit_engagement(engagement, str(uuid.uuid4()))

        # Assert
        sd_updater.edit_engagement_profession.assert_not_called()

    @given(
        status=st.sampled_from(["1", "S"]),
        from_date=st.datetimes(),
        to_date=st.datetimes() | st.none(),
    )
    @patch("sdlon.sd_common.sd_lookup_settings")
    @patch("sdlon.sd_changed_at.sd_lookup")
    def test_timestamps_read_employment_changed(
        self,
        mock_sd_lookup,
        sd_settings,
        status,
        from_date,
        to_date,
    ):
        """Test that calls contain correct ActivationDate and ActivationTime"""
        sd_settings.return_value = ("", "", "")

        sd_updater = setup_sd_changed_at()
        sd_updater.read_employment_changed(from_date=from_date, to_date=to_date)
        expected_url = "GetEmploymentChangedAtDate20111201"
        url = mock_sd_lookup.call_args.args[0]
        params = mock_sd_lookup.call_args.kwargs["params"]
        self.assertEqual(url, expected_url)
        self.assertEqual(params["ActivationDate"], from_date.strftime("%d.%m.%Y"))
        self.assertEqual(params["ActivationTime"], from_date.strftime("%H:%M"))
        if to_date:
            self.assertEqual(params["DeactivationDate"], to_date.strftime("%d.%m.%Y"))
            self.assertEqual(params["DeactivationTime"], to_date.strftime("%H:%M"))

    @given(
        status=st.sampled_from(["1", "S"]),
        from_date=st.datetimes(),
        to_date=st.datetimes() | st.none(),
    )
    @patch("sdlon.sd_common.sd_lookup_settings")
    @patch("sdlon.sd_changed_at.sd_lookup")
    def test_timestamps_get_sd_persons_changed(
        self,
        mock_sd_lookup,
        sd_settings,
        status,
        from_date,
        to_date,
    ):
        """Test that calls contain correct ActivationDate and ActivationTime"""
        sd_settings.return_value = ("", "", "")

        sd_updater = setup_sd_changed_at()
        sd_updater.get_sd_persons_changed(from_date=from_date, to_date=to_date)
        expected_url = "GetPersonChangedAtDate20111201"
        url = mock_sd_lookup.call_args.args[0]
        params = mock_sd_lookup.call_args.kwargs["params"]
        self.assertEqual(url, expected_url)
        self.assertEqual(params["ActivationDate"], from_date.strftime("%d.%m.%Y"))
        self.assertEqual(params["ActivationTime"], from_date.strftime("%H:%M"))
        if to_date:
            self.assertEqual(params["DeactivationDate"], to_date.strftime("%d.%m.%Y"))
            self.assertEqual(params["DeactivationTime"], to_date.strftime("%H:%M"))

    def test_fix_department_called_with_date(self):
        # Arrange
        sd_updater = setup_sd_changed_at()
        fix_date = datetime.datetime.today() + datetime.timedelta(weeks=80)
        sd_updater.helper.read_ou.return_value = {"status": "found"}

        # Act
        sd_updater.apply_NY_logic(
            "00000000-0000-0000-0000-000000000000", "job_id", None, "person_uuid"
        )

        # Assert
        sd_updater.fix_departments_mock.fix_department.assert_called_once_with(
            "00000000-0000-0000-0000-000000000000", fix_date.date()
        )


def test_read_forced_uuid_use_empty_dict():
    sd_updater = setup_sd_changed_at({"sd_read_forced_uuids": False})
    assert sd_updater.employee_forced_uuids == dict()


def test_updater_field_is_none_when_primary_engagement_calc_disabled():
    sd_updater = setup_sd_changed_at({"sd_update_primary_engagement": False})
    assert sd_updater.updater is None


@pytest.mark.parametrize(
    "too_deep,expected_target_ou",
    [
        ([], "00000000-0000-0000-0000-000000000000"),
        (
            ["Afdelings-niveau"],
            "10000000-0000-0000-0000-000000000000",
        ),
        (
            ["Afdelings-niveau", "NY1-niveau"],
            "20000000-0000-0000-0000-000000000000",
        ),
    ],
)
def test_apply_ny_logic(too_deep: list[str], expected_target_ou: str) -> None:
    """
    Test the case where an SD employment is moved to a new SD department, which
    is an "Afdelings-niveau". The apply_NY_logic function should then return
    the UUID of the first "NY-niveau" which is not in the "too_deep" list.
    """
    # Arrange
    sd_updater = setup_sd_changed_at({"sd_import_too_deep": too_deep})

    ou_uuid_afd = "00000000-0000-0000-0000-000000000000"
    ou_uuid_ny1 = "10000000-0000-0000-0000-000000000000"
    ou_uuid_ny2 = "20000000-0000-0000-0000-000000000000"
    ou_uuid_ny3 = "30000000-0000-0000-0000-000000000000"
    person_uuid = str(uuid.uuid4())

    sd_updater.helper.read_ou = MagicMock(
        return_value={
            "uuid": ou_uuid_afd,
            "org_unit_level": {"user_key": "Afdelings-niveau"},
            "parent": {
                "uuid": ou_uuid_ny1,
                "org_unit_level": {"user_key": "NY1-niveau"},
                "parent": {
                    "uuid": ou_uuid_ny2,
                    "org_unit_level": {"user_key": "NY2-niveau"},
                    "parent": {
                        "uuid": ou_uuid_ny3,
                        "org_unit_level": {"user_key": "NY3-niveau"},
                        "parent": None,
                    },
                },
            },
        }
    )
    sd_updater.create_association = MagicMock()

    # Act
    target_ou_uuid = sd_updater.apply_NY_logic(
        ou_uuid_afd, 12345, {"from": "2023-08-01", "to": None}, person_uuid
    )

    # Assert
    assert target_ou_uuid == expected_target_ou
