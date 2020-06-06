import unittest
import datetime

from app.src import db
from app.src.states.models import State
from app.src.users.models import User
from app.tests.base import BaseTestCase


def empty_table(model):
    for one_instance in model.query.all():
        db.session.delete(one_instance)


class TestUserModel(BaseTestCase):
    def setUp(self):
        super().setUp()

    def test_user_creation_and_state_relation(self):
        state = State(code=133, name="tesa")
        db.session.add(state)
        db.session.commit()
        expected_saved_user = {
            "name": "Yari Taft",
            "age": 24,
            "state": state,
            "created_at": datetime.datetime.utcnow().date(),
            "updated_at": datetime.datetime.utcnow().date(),
        }
        my_saved_state = State.query.first()
        user = User(name="Yari Taft", age=24, state_id=state.id,)
        db.session.add(user)
        db.session.commit()
        my_saved_user = User.query.first()
        saved_user_attrs = {
            "name": my_saved_user.name,
            "age": my_saved_user.age,
            "state": my_saved_user.state,
            "created_at": my_saved_user.created_at.date(),
            "updated_at": my_saved_user.updated_at.date(),
        }
        self.assertTrue(State.query.filter_by(code=133).first() == state)
        self.assertTrue(User.query.first() == user)
        self.assertTrue(saved_user_attrs == expected_saved_user)


if __name__ == "__main__":
    unittest.main()
