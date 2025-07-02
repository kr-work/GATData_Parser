import pathlib

from sqlalchemy import create_engine

file_path = pathlib.Path(__file__).parents[1]
file_path /= "./src/state_data.sqlite3"
sqlite_url = f"sqlite:///{file_path}"


engine = create_engine(url=sqlite_url, echo=False)