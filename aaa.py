import tomllib
from pathlib import Path

with (Path(__file__).parent / "config.toml").open("rb") as f: # pathlib最高の瞬間
    toml = tomllib.load(f)
    
    print(Path(toml["path"]["log_folder"]).exists())