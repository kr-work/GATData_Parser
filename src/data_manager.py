import get_dc1_data
import get_dc3_data
from crud import CreateData, ReadData
from pathlib import Path


class DataManager:
    def __init__(self):
        self.create_data: CreateData = CreateData()
        self.read_data: ReadData = ReadData()

    def store_dc1_data(self, file_path: Path):
        all_data = get_dc1_data.get_match_data(file_path)
        if not all_data:
            print(f"No data found in file: {file_path}")
            return

        for data in all_data:
            end = data[0]
            shot = data[1]
            my_team_stones_data = data[2]
            opponent_stones_data = data[3]
            my_team_scores_data = data[4]
            opponent_scores_data = data[5]

            self.create_data.create_state_data(
                end=end,
                shot=shot,
                my_team_stones=my_team_stones_data,
                opponent_team_stones=opponent_stones_data,
                my_team_scores=my_team_scores_data,
                opponent_team_scores=opponent_scores_data
            )            
        
    def store_dc3_data(self, file_path: Path, end: int, shot: int):
        data = get_dc3_data.get_specific_end_shot_data(file_path, end, shot)
        my_team_stones_data = []
        opponent_stones_data = []
        my_team_scores_data = []
        opponent_scores_data = []

        if data is None:
            print(f"No data found for end {end} and shot {shot}")
            return
        else:
            my_team_stones_data, opponent_stones_data, my_team_scores_data, opponent_scores_data = data

        self.create_data.create_state_data(
            end=end,
            shot=shot,
            my_team_stones=my_team_stones_data,
            opponent_team_stones=opponent_stones_data,
            my_team_scores=my_team_scores_data,
            opponent_team_scores=opponent_scores_data
        )


    def read_data(self, end: int, shot: int):
        return self.read_data.read_state_data(end, shot)
    

if __name__ == "__main__":
    data_manager = DataManager()

    dir_path = Path(__file__).parents[1] / "DC3_GATData"
    file_path_list = list(dir_path.glob("**/**/game.dcl2"))
    for end in range(10):
        for shot in range(16):
            for file_path in file_path_list:
                print(f"Processing file: {file_path}")
                data_manager.store_dc3_data(file_path, end, shot)

    dir_path = Path(__file__).parents[1] / "DC_GATData"
    files_path = [p for p in dir_path.glob("**/*.dcl") if "!" not in str(p)]
    for file_path in files_path:
        print(f"Processing file: {file_path}")
        data_manager.store_dc1_data(file_path)

