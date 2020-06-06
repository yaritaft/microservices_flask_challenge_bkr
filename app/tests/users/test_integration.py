from datetime import datetime
import json
import unittest
from copy import deepcopy

from dateutil.parser import parse

from app.src import db
from app.src.states.models import State
from app.src.users.models import User
from app.tests.base import BaseTestCase


class TestUsersBase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.valid_type = "application/json"

        self.expected_response = {
            "name": "yari taft",
            "age": 25,
            "id": 1,
            "state_id": 1,
            "created_at": datetime.utcnow().date(),
            "updated_at": datetime.utcnow().date(),
        }

        self.client.post(
            "/states/",
            data=json.dumps({"name": "Barracas", "code": 237}),
            content_type=self.valid_type,
        )

    def _from_raw_dict_to_parsed_dict(self, response):
        parsed_response = deepcopy(response.data)
        parsed_response = json.loads(parsed_response)["data"]
        for key in ("created_at", "updated_at"):
            parsed_response[key] = parse(parsed_response[key]).date()
        return parsed_response

    def _post_user(self):
        self.client.post(
            "/users/",
            data=json.dumps({"name": "yari taft", "age": 25, "state_id": 1}),
            content_type=self.valid_type,
        )


class TestUsersPost(TestUsersBase):
    def test_user_creation_successful_integration(self):
        response = self.client.post(
            "/users/",
            data=json.dumps({"name": "yari taft", "age": 237, "state_id": 1}),
            content_type=self.valid_type,
        )

        self.assertEqual(response.status_code, 201)

    def test_user_creation_wrong_data_integration(self):
        response = self.client.post(
            "/users/",
            data=json.dumps({"name": 237, "age": 237, "state_id": 1}),
            content_type=self.valid_type,
        )

        self.assert400(response)

    def test_user_creation_missing_data_integration(self):
        response = self.client.post(
            "/users/",
            data=json.dumps({"age": 237}),
            content_type=self.valid_type,
        )

        self.assert400(response)

    def test_user_creation_non_existent_state_integration(self):
        response = self.client.post(
            "/users/",
            data=json.dumps({"name": 237, "age": 237, "state_id": 12}),
            content_type=self.valid_type,
        )

        self.assert400(response)

    def test_user_creation_non_json_integration(self):
        response = self.client.post(
            "/users/",
            data=json.dumps({"name": 237, "age": 237, "state_id": 12}),
        )

        self.assert400(response)

    def test_user_creation_wrong_content_type_integration(self):
        response = self.client.post(
            "/users/",
            data=json.dumps({"name": 237, "age": 237, "state_id": 12}),
            content_type="application/x-www-form-urlencoded",
        )

        self.assert400(response)


class TestUsersGets(TestUsersBase):
    def test_get_specific_user_successful_integration(self):
        self._post_user()
        response = self.client.get("/users/1", content_type=self.valid_type)

        parsed_response = self._from_raw_dict_to_parsed_dict(response)

        self.assert_200(response)
        self.assertEqual(self.expected_response, parsed_response)

    def test_get_list_of_users_successful_integration(self):
        self._post_user()
        response = self.client.get("/users/", content_type=self.valid_type)

        parsed_response = json.loads(response.data)["data"]
        self.assert_200(response)
        self.assertEqual(1, len(parsed_response))


class TestUsersDeletion(TestUsersBase):
    def test_delete_user_successful_integration(self):
        self._post_user()
        response = self.client.delete("/users/1", content_type=self.valid_type)

        self.assert_200(response)


class TestUserUpdate(TestUsersBase):
    def test_patch_user_successful_integration(self):
        self._post_user()
        response = self.client.patch(
            "/users/1",
            data=json.dumps({"name": "other_name"}),
            content_type=self.valid_type,
        )
        patched_resource = self.client.get(
            "/users/1", content_type=self.valid_type
        )
        patched_resource = json.loads(patched_resource.data)["data"]
        self.assert_200(response)
        self.assertEqual(patched_resource["name"], "other_name")

    def test_patch_wrong_data_type_integration(self):
        self._post_user()
        response = self.client.patch(
            "/users/1",
            data=json.dumps({"name": 237}),
            content_type=self.valid_type,
        )
        not_patched_resource = self.client.get(
            "/users/1", content_type=self.valid_type
        )
        not_patched_resource = json.loads(not_patched_resource.data)["data"]
        self.assert_400(response)
        self.assertEqual(not_patched_resource["name"], "yari taft")

    def test_patch_try_to_change_id_integration(self):
        self._post_user()
        response = self.client.patch(
            "/users/1",
            data=json.dumps({"id": 2344}),
            content_type=self.valid_type,
        )
        not_patched_resource = self.client.get(
            "/users/1", content_type=self.valid_type
        )
        not_patched_resource = json.loads(not_patched_resource.data)["data"]
        self.assert_400(response)
        self.assertEqual(not_patched_resource["id"], 1)


if __name__ == "__main__":
    unittest.main()
