from pathlib import Path
import json
import os

try:
    from variables import Variable

    variable = Variable()

except ModuleNotFoundError or ImportError as e:
    print(f"Error in Importing: {e}")


class Hashmap:
    def __init__(self, path: Path) -> None:
        self.path = path
        return None

    def find_json_file(self, data_file_path) -> bool:
        return os.path.exists(data_file_path)

    def load_json_file(self, data_file_path) -> dict:
        try:
            with open(data_file_path, "r") as json_file:
                file_list = json.load(json_file)
            return file_list
        except FileNotFoundError as e:
            return f"Error in Loading Json File: File Not Found"

    def create_json_file(self, search_path, data_file_path) -> dict:
        if not self.find_json_file(data_file_path):
            file_list = {}

            for root, _, files in os.walk(search_path):
                for file in files:
                    file_list[file] = os.path.join(root, file)

            with open(data_file_path, "w") as json_file:
                json.dump(file_list, json_file)

            return file_list
        else:
            return self.load_json_file(data_file_path)
