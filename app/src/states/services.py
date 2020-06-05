
import uuid
import datetime

from app.src import db
from app.src.states.models import State


def save_new_state(data):
    state = State.query.filter_by(id=data['id']).first()
    if not state:
        new_state = State(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'State already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return State.query.all()


def get_a_user(public_id):
    return State.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()