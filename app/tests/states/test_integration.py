from datetime import datetime
import json
import unittest
from copy import deepcopy

from dateutil.parser import parse

from app.src import db
from app.src.states.models import State
from app.src.users.models import User
from app.tests.base import BaseTestCase


class TestStatesBase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.valid_type = "application/json"

        self.expected_response = {
            "name": "Barracas",
            "code": 444,
            "id": 1,
            "created_at": datetime.utcnow().date(),
            "updated_at": datetime.utcnow().date(),
        }

    def _from_raw_dict_to_parsed_dict(self, response):
        parsed_response = deepcopy(response.data)
        parsed_response = json.loads(parsed_response)["data"]
        for key in ("created_at", "updated_at"):
            parsed_response[key] = parse(parsed_response[key]).date()
        return parsed_response

    def _post_state(self):
        self.client.post(
            "/states/",
            data=json.dumps({"name": "Barracas", "code": 444}),
            content_type=self.valid_type,
        )


class TestStatesPost(TestStatesBase):
    def test_state_creation_successful_integration(self):
        response = self.client.post(
            "/states/",
            data=json.dumps({"name": "Barracas", "code": 444}),
            content_type=self.valid_type,
        )

        self.assertEqual(response.status_code, 201)

    def test_state_creation_wrong_data_integration(self):
        response = self.client.post(
            "/states/",
            data=json.dumps({"name": 44, "code": 444}),
            content_type=self.valid_type,
        )

        self.assert400(response)

    def test_state_creation_missing_data_integration(self):
        response = self.client.post(
            "/states/",
            data=json.dumps({"code": 444}),
            content_type=self.valid_type,
        )

        self.assert400(response)

    def test_state_creation_integration_not_json(self):
        response_without_content_type = self.client.post(
            "/states/", data=json.dumps({"name": "Barracas", "code": 444}),
        )

        response_with_wrong_content_type = self.client.post(
            "/states/",
            data=json.dumps({"name": "Barracas", "code": 444}),
            content_type="application/x-www-form-urlencoded",
        )

        self.assert400(response_without_content_type)
        self.assert400(response_with_wrong_content_type)


class TestStatesGets(TestStatesBase):
    def test_get_specific_state_successful_integration(self):
        self._post_state()
        response = self.client.get("/states/1", content_type=self.valid_type)

        parsed_response = self._from_raw_dict_to_parsed_dict(response)

        self.assert_200(response)
        self.assertEqual(self.expected_response, parsed_response)

    def test_get_list_of_states_successful_integration(self):
        self._post_state()
        response = self.client.get("/states/", content_type=self.valid_type)

        parsed_response = json.loads(response.data)["data"]
        print(parsed_response)
        self.assert_200(response)
        self.assertEqual(1, len(parsed_response))


class TestStatesDeletion(TestStatesBase):
    def test_delete_state_successful_integration(self):
        self._post_state()
        response = self.client.delete(
            "/states/1", content_type=self.valid_type
        )

        self.assert_200(response)


class TestStatesUpdate(TestStatesBase):
    def test_patch_state_successful_integration(self):
        self._post_state()
        response = self.client.patch(
            "/states/1",
            data=json.dumps({"name": "other_name"}),
            content_type=self.valid_type,
        )
        patched_resource = self.client.get(
            "/states/1", content_type=self.valid_type
        )
        patched_resource = json.loads(patched_resource.data)["data"]
        self.assert_200(response)
        self.assertEqual(patched_resource["name"], "other_name")

    def test_patch_wrong_data_type_integration(self):
        self._post_state()
        response = self.client.patch(
            "/states/1",
            data=json.dumps({"name": 444}),
            content_type=self.valid_type,
        )
        not_patched_resource = self.client.get(
            "/states/1", content_type=self.valid_type
        )
        not_patched_resource = json.loads(not_patched_resource.data)["data"]
        self.assert_400(response)
        self.assertEqual(not_patched_resource["name"], "Barracas")

    def test_patch_try_to_change_id_integration(self):
        self._post_state()
        response = self.client.patch(
            "/states/1",
            data=json.dumps({"id": 2344}),
            content_type=self.valid_type,
        )
        not_patched_resource = self.client.get(
            "/states/1", content_type=self.valid_type
        )
        not_patched_resource = json.loads(not_patched_resource.data)["data"]
        self.assert_400(response)
        self.assertEqual(not_patched_resource["id"], 1)


if __name__ == "__main__":
    unittest.main()
