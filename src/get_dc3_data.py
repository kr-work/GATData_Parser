import json
from pprint import pprint

from pathlib import Path


def get_specific_end_shot_data(
    data_dir: Path,
    end: int,
    shot: int,
):
    """Parses the match data for a specific end and shot from a .dcl2 file.
    Args:
        data_dir (Path): The path to the .dcl2 file.
        end (int): The end number.
        shot (int): The shot number.
    Returns:
        tuple: A tuple containing:
            - my_team_stones_data (list): List of stones for my team.
            - opponent_stones_data (list): List of stones for the opponent team.
            - my_team_scores_data (list): List of scores for my team.
            - opponent_scores_data (list): List of scores for the opponent team.
    """
    match_data: list = []
    with open(data_dir, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("{"):
                match_data.append(json.loads(line))
                # break

    my_team_stones_data: list = []
    opponent_stones_data: list = []
    my_team_scores_data: list = []
    opponent_scores_data: list = []
    next_move_team: str = ""

    for data in match_data:
        if ("state" in data["log"]):
            if data["log"]["state"]["end"] == end and data["log"]["state"]["shot"] == shot:
                next_move_team = data["log"]["next_team"]
                team0_stones = data["log"]["state"]["stones"]["team0"]
                team1_stones = data["log"]["state"]["stones"]["team1"]
                team0_stones_data = []
                team0_scores_data = []
                team1_stones_data = []
                team1_scores_data = []

                for stone in team0_stones:
                    if stone is None:
                        team0_stones_data.append([0.0, 0.0])
                    else:
                        team0_stones_data.append([stone["position"]["x"], stone["position"]["y"]])
                for stone in team1_stones:
                    if stone is None:
                        team1_stones_data.append([0.0, 0.0])
                    else:
                        team1_stones_data.append([stone["position"]["x"], stone["position"]["y"]])

                for i in range(10):
                    team0_score = data["log"]["state"]["scores"]["team0"][i]
                    team1_score = data["log"]["state"]["scores"]["team1"][i]
                    if team0_score is None:
                        team0_scores_data.append(0)
                    else:
                        team0_scores_data.append(team0_score)
                    if team1_score is None:
                        team1_scores_data.append(0)
                    else:
                        team1_scores_data.append(team1_score)

                if next_move_team == "team0":
                    my_team_stones_data = team0_stones_data
                    opponent_stones_data = team1_stones_data
                    my_team_scores_data = team0_scores_data
                    opponent_scores_data = team1_scores_data
                elif next_move_team == "team1":
                    my_team_stones_data = team1_stones_data
                    opponent_stones_data = team0_stones_data
                    my_team_scores_data = team1_scores_data
                    opponent_scores_data = team0_scores_data
                
                break

    return (
        my_team_stones_data,
        opponent_stones_data,
        my_team_scores_data,
        opponent_scores_data,
    )


if __name__ == "__main__":
    data_dir = Path("../GATData/")
    end: int = 9
    shot: int = 15
    dcl2files: list = (list(data_dir.glob("**/**/game.dcl2")))
    for dcl2file in dcl2files:
        get_specific_end_shot_data(dcl2file, end, shot)
        break
