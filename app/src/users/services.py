from app.src import db
from app.src.states.models import State
from app.src.users.models import User


def save_new_user(data):
    """Save new user and generate response.

    Parameters
    ----------
    data : dict
        payload to use in order to update user.

    Returns
    -------
    Tuple (dict, int)
        Response object and status code. (dict, int)
        200 If user was created
        400 If state does not exist.
    """
    state = State.query.filter_by(id=data["state_id"]).first()
    if state is None:
        return (None, 400)
    new_user = User(
        name=data["name"], age=data["age"], state_id=data["state_id"]
    )
    save_changes(new_user)
    response_object = {
        "status": "success",
        "message": "Successfully registered.",
    }
    return response_object, 201


def get_all_users():
    """Get saved users.

    Returns
    -------
    Query
        query object with users instances.
    """
    return User.query.all()


def get_a_user(user_id):
    """Get saved user.

    Parameters
    ----------
    user_id : int
        user identifier.

    Returns
    -------
    User
        user model instance saved.
    """
    return User.query.filter_by(id=user_id).first()


def save_changes(user):
    """Save user.

    Parameters
    ----------
    user : User
        user model instance saved.
    """
    db.session.add(user)
    db.session.commit()


def update_user(user, data):
    """Update saved user.

    Parameters
    ----------
    user : User
        user model instance saved.
    data : dict
        payload to use in order to update user.
    """
    if data.get("id") is not None:
        return 400
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()


def delete_user(user):
    """Delete saved user.

    Parameters
    ----------
    user : User
        user model saved instance.
    """
    db.session.delete(user)
    db.session.commit()
