import get_dc3_data

from sqlalchemy.orm import Session
from sqlalchemy import select
from DataBase import StateData, Base
from create_sqlite_engine import engine


class CreateData:
    def __init__(self):
        pass

    def create_table(self):
        try:
            Base.metadata.create_all(engine)
        except Exception as e:
            print(f"Error creating table: {e}")

    def create_state_data(
            self,
            end: int,
            shot: int,
            my_team_stones: list,
            opponent_team_stones: list,
            my_team_scores: list,
            opponent_team_scores: list
    ):
        self.create_table()
        try:
            with Session(engine) as session:
                state_data = StateData(
                    end=end,
                    shot=shot,
                    my_team_stones=my_team_stones,
                    opponent_team_stones=opponent_team_stones,
                    my_team_scores=my_team_scores,
                    opponent_team_scores=opponent_team_scores
                )
                session.add(state_data)
                session.commit()
        except Exception as e:
            print(f"Error creating state data: {e}")


class ReadData:
    def __init__(self):
        pass

    def read_state_data(self, end: int, shot: int):
        try:
            with Session(engine) as session:
                stmt = select(StateData).where(StateData.end == end, StateData.shot == shot)
                result = session.execute(stmt).scalars().all()
                if result:
                    return result
                else:
                    print(f"No data found for end {end} and shot {shot}")
                    return None
        except Exception as e:
            print(f"Error reading state data: {e}")
            return None
