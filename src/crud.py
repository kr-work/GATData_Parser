from pprint import pprint

from sqlalchemy.orm import Session
from sqlalchemy import select
from model.DataBase import StateData, Base
from model.DataModel import StateDataModel
from create_sqlite_engine import engine


class CreateData:
    """Handles the creation of state data in the database."""
    def __init__(self):
        pass

    def create_table(self):
        """Creates the state data table if it does not exist."""
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
        """Creates a new state data entry in the database.
        Args:
            end (int): The end number.
            shot (int): The shot number.
            my_team_stones (list): List of stones for my team.
            opponent_team_stones (list): List of stones for the opponent team.
            my_team_scores (list): List of scores for my team.
            opponent_team_scores (list): List of scores for the opponent team.
        """
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
    """Handles reading state data from the database."""
    def __init__(self):
        pass

    def read_state_data(self, end: int, shot: int):
        """Reads state data for a specific end and shot from the database.
        Args:
            end (int): The end number.
            shot (int): The shot number.
        Returns:
            list: A list of StateDataModel instances containing the state data.
        """
        try:
            with Session(engine) as session:
                stmt = select(StateData).where(StateData.end == end, StateData.shot == shot)
                result = session.execute(stmt).scalars().all()
                if result:
                    data = []
                    for item in result:
                        data.append(StateDataModel.model_validate(item.__dict__))
                    return data
                else:
                    print(f"No data found for end {end} and shot {shot}")
                    return None
        except Exception as e:
            print(f"Error reading state data: {e}")
            return None
        
if __name__ == "__main__":
    read_data = ReadData()
    data = read_data.read_state_data(9, 15)
    for item in data:
        pprint(item.model_dump())
    
