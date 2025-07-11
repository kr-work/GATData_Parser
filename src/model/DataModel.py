from pydantic import BaseModel

class StateDataModel(BaseModel):
    id: int
    end: int
    shot: int
    my_team_stones: list
    opponent_team_stones: list
    my_team_scores: list
    opponent_team_scores: list