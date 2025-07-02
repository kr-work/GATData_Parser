from pprint import pprint

from pathlib import Path

def get_match_data(data_dir: Path):
    match_data: list = []
    shot: int = 0
    end: int = 0
    next_shot_team: str = "0"
    stones_data = []
    team0_scores_data: list = [0] * 10
    team1_scores_data: list = [0] * 10

    with open(data_dir, "r", encoding="utf-8") as file:
        
        lines = [line.strip() for line in file]

    for line in lines:
        if line.startswith("["):
            numbers = line[1:5]
            if numbers == "Game":
                continue
            end = int(numbers[:2])
            shot = int(numbers[2:])
            # print(f"end: {end}, shot: {shot}")

        elif line.startswith("POSITION"):
            stones_data = line.split(" ")[1:]
            # print(f"stones_data: {stones_data}")
            team0_stones_data: list = []
            team1_stones_data: list = []
            state_data: list = []

            for i in range(0, 32, 2):
                position_x = float(stones_data[i])
                position_y = float(stones_data[i + 1])
                if i % 4 == 0:
                    if position_x == 0.0 and position_y == 0.0:
                        team0_stones_data.append([0.0, 0.0])
                    else:
                        team0_stones_data.append([float(stones_data[i]) - 2.375, 43.284 - float(stones_data[i + 1])]) # X = x - 2.375, Y = 3.05 - y + 40.234
                elif i % 4 == 2:
                    if position_x == 0.0 and position_y == 0.0:
                        team1_stones_data.append([0.0, 0.0])
                    else:
                        team1_stones_data.append([float(stones_data[i]) - 2.375, 43.284 - float(stones_data[i + 1])])
            
            state_data.append(end)
            state_data.append(shot)

            if next_shot_team == "0":
                state_data.append(team0_stones_data)
                state_data.append(team1_stones_data)
                state_data.append(team0_scores_data)
                state_data.append(team1_scores_data)
            elif next_shot_team == "1":
                state_data.append(team1_stones_data)
                state_data.append(team0_stones_data)
                state_data.append(team1_scores_data)
                state_data.append(team0_scores_data)

            match_data.append(state_data)

        elif line.startswith("SETSTATE"):
            next_shot_team = line.split(" ")[4:][0]
            # print(f"next_shot_team: {next_shot_team}")

        elif line.startswith("SCORE"):
            score_data = line.split(" ")[1:2]
            score_data = score_data[0]
            score_data = int(score_data)
            if score_data > 0:
                team0_scores_data[end] = score_data
            elif score_data < 0:
                team1_scores_data[end] = abs(score_data)

    # print(f"team0_stones_all_data: {team0_stones_all_data}")
    # print(f"team1_stones_all_data: {team1_stones_all_data}")

            

    return match_data


if __name__ == "__main__":
    dir_path = Path(__file__).parents[1] / "DC1_GATData"
    file_path = dir_path / "UEC1_100_log" / "Ayumu - ChickenRamen" / "Ayumu0308 - ChickenRamen [2015-04-23 120854].dcl"
    # dclfile_path_list = [p for p in dir_path.glob("**/.dcl") if "!" not in str(p)]
    # pprint(dclfile_path_list)
    # print(file_path)
    match_data = get_match_data(file_path)
    # pprint(match_data)