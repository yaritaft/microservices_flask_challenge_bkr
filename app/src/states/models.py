from sqlalchemy import Column, create_engine, Integer, String, Date, Sequence
from sqlalchemy.orm import relationship

from . import Base

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, Sequence('state_id_seq', primary_key=True)
    code = Column(Integer)
    name = Column(String)
    state_ = relationship("State")
    updated_at = Column(Date)
    created_at = Column(Date)
    def __repr__(self):
        return "<State(name='%s')>" % (
            self.name,
        )