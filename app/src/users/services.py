from app.src import db
from app.src.users.models import User


def save_new_user(data):
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
    return User.query.all()


def get_a_user(user_id):
    return User.query.filter_by(id=user_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def update_user(user, data):
    data.pop("id", None)
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()


def delete_user(user):
    db.session.delete(user)
    db.session.commit()
