import os
from sqlalchemy import Column, create_engine, Integer, String, Date, Sequence
from sqlalchemy.orm import relationship

engine = create_engine(os.getenv("DATABASE_URL")
Base = declarative_base()

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