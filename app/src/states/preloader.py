from app.src import db

from .models import State


def from_csv_to_dict(reader):
    """Drop first line and transform from csv to dict."""
    next(reader)
    new_dict = {}
    for row in reader:
        key, value = row[0].split(";")[0], row[0].split(";")[1]
        new_dict[key] = value
    return new_dict


def preload_data(reader):
    if State.query.first() is None:
        states = from_csv_to_dict(reader)
        for code, state in states.items():
            new_state = State(code=code, name=state)
            db.session.add(new_state)
            db.session.commit()
