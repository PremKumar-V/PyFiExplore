from pathlib import Path
import json
import os

try:
    from variables import Variable

    variable = Variable()

except ModuleNotFoundError or ImportError as e:
    print(f"Error in Importing: {e}")


class Hashmap:
    def __init__(self, path: Path, path_for_saving: Path) -> None:
        """
        @arguments
        path = path for directory json file
        path_for_saving = path that defines which directory to save

        @returns None
        """

        self.data_file_path: Path = path
        self.path_for_saving: Path = path_for_saving
        return None

    def find_json_file(self) -> bool:
        """
        @return boolean that defines if directory json is already present
        """

        return os.path.exists(self.data_file_path)

    def load_json_file(self) -> dict:
        """
        @returns dictionary or json of directory json
        """

        try:
            with open(self.data_file_path, "r") as json_file:
                file_list = json.load(json_file)
            return file_list
        except FileNotFoundError as e:
            return f"Error in Loading Json File: File Not Found"

    def create_json_file(self) -> dict:
        """
        @returns creates and returns directory or json
        """

        file_list = {}
        dir_list = {}
        structure = {}

        for dirpath, dirnames, filenames in os.walk(self.path_for_saving):
            for filename in filenames:
                file_list[filename] = os.path.join(dirpath, filename)

            for dirname in dirnames:
                dir_list[dirname] = os.path.join(dirpath, dirname)

        structure["files"] = file_list
        structure["directories"] = dir_list

        with open(self.data_file_path, "w") as json_file:
            json.dump(structure, json_file)

        return structure

    def create_and_load_json_file(self) -> dict:
        """
        @return dictionary or json file of directory jsonn file
        """

        if not self.find_json_file():
            return self.create_json_file()
        else:
            return self.load_json_file()
