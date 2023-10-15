from pathlib import Path
import json
import os

try:
    from variables import Variable

    variable = Variable()

except ModuleNotFoundError or ImportError as e:
    print(f"Error in Importing: {e}")


class Hashmap:
    def __init__(self, path: Path, search_path: Path) -> None:
        self.data_file_path = path
        self.search_path = search_path
        return None

    def find_json_file(self) -> bool:
        return os.path.exists(self.data_file_path)

    def load_json_file(self) -> dict:
        try:
            with open(self.data_file_path, "r") as json_file:
                file_list = json.load(json_file)
            return file_list
        except FileNotFoundError as e:
            return f"Error in Loading Json File: File Not Found"

    def create_json_file(self) -> dict:
        if not self.find_json_file():
            file_list = {}

            for root, _, files in os.walk(self.search_path):
                for file in files:
                    file_list[file] = os.path.join(root, file)

            with open(self.data_file_path, "w") as json_file:
                json.dump(file_list, json_file)

            return file_list
        else:
            return self.load_json_file()
