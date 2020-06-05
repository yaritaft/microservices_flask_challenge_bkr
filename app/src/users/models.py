from datetime import datetime

from .. import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, db.Sequence("user_id_seq"), primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    state_id = db.Column(db.Integer, db.ForeignKey("state.id"), nullable=False)
    state = db.relationship("State")
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<User(name='%s')>" % (self.name,)
