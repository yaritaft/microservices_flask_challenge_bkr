from datetime import datetime

from .. import db


class State(db.Model):
    __tablename__ = "state"
    id = db.Column(db.Integer, db.Sequence("state_id_seq"), primary_key=True)
    code = db.Column(db.Integer, unique=True)
    name = db.Column(db.String)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<State(name='%s')>" % (self.name,)
