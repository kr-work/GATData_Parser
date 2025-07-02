from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, Float, JSON


class Base(DeclarativeBase):
    pass


class StateData(Base):
    __tablename__ = 'state_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    end = Column(Integer)
    shot = Column(Integer)
    my_team_stones = Column(JSON)
    opponent_team_stones = Column(JSON)
    my_team_scores = Column(JSON)
    opponent_team_scores = Column(JSON)