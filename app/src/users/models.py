from sqlalchemy import Column, create_engine, Integer, String, Date, Sequence
from sqlalchemy.orm import relationship

from . import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq', primary_key=True)
    name = Column(String)
    age = Column(Integer)
    state_ = relationship("State")
    updated_at = Column(Date)
    created_at = Column(Date)
    def __repr__(self):
        return "<User(name='%s')>" % (
            self.name,
        )
