from pathlib import Path
import yaml

class ConfigParser:
    def __init__(self, file_path: Path | str):
        self.file_path = Path(file_path)
    def parse(self) -> dict:
        with open(self.file_path, 'r') as file:
            config_parsed = yaml.safe_load(file)
        return config_parsed