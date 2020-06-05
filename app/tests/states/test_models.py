import unittest
import datetime

from app.src import db
from app.src.states.models import State
from app.src.users.models import User
from app.tests.base import BaseTestCase


class TestStateModel(BaseTestCase):

    def test_state_creation(self):
        state = State(
            code=133,
            name='tesa'
        )
        db.session.add(state)
        db.session.commit()
        my_saved_state = State.query.filter_by(code=133).first()
        print(state)
        print(my_saved_state)
        self.assertTrue(my_saved_state==state)

if __name__ == '__main__':
    unittest.main()
