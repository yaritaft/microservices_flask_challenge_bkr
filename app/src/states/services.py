from app.src import db
from app.src.states.models import State


def save_new_state(data):
    new_state = State(name=data["name"], code=data["code"])
    save_changes(new_state)
    response_object = {
        "status": "success",
        "message": "Successfully registered.",
    }
    return response_object, 201


def get_all_states():
    return State.query.all()


def get_a_state(state_id):
    return State.query.filter_by(id=state_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def update_state(state, data):
    data.pop("id", None)
    for key, value in data.items():
        setattr(state, key, value)
    db.session.commit()


def delete_state(state):
    db.session.delete(state)
    db.session.commit()
