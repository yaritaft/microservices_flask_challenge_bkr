from app.src import db
from app.src.states.models import State


def save_new_state(data):
    """Save new state and generate response.

    Parameters
    ----------
    data : dict
        payload to use in order to update state.

    Returns
    -------
    Tuple (dict, int)
        Response object and status code. (dict, int)
    """
    new_state = State(name=data["name"], code=data["code"])
    save_changes(new_state)
    response_object = {
        "status": "success",
        "message": "Successfully registered.",
    }
    return response_object, 201


def get_all_states():
    """Get saved states.

    Returns
    -------
    Query
        query object with states instances.
    """
    return State.query.all()


def get_a_state(state_id):
    """Get saved state.

    Parameters
    ----------
    state_id : int
        state identifier.

    Returns
    -------
    State
        state model instance saved.
    """
    return State.query.filter_by(id=state_id).first()


def save_changes(data):
    """Save state.

    Parameters
    ----------
    state : State
        state model instance saved.
    """
    db.session.add(data)
    db.session.commit()


def update_state(state, data):
    """Update saved state.

    Parameters
    ----------
    state : State
        state model instance saved.
    data : dict
        payload to use in order to update state.
    """
    data.pop("id", None)
    for key, value in data.items():
        setattr(state, key, value)
    db.session.commit()


def delete_state(state):
    """Delete saved state.

    Parameters
    ----------
    state : State
        state model saved instance.
    """
    db.session.delete(state)
    db.session.commit()
