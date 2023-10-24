from variables import Variable
from hashmap import Hashmap

from pathlib import Path

variable = Variable()


def search_file(search_term: Path, is_folder: bool) -> str:
    hashmap = Hashmap(variable.data_file_path, variable.search_path)

    structure = hashmap.create_json_file()

    try:
        if not is_folder:
            return structure["files"][search_term]

        return structure["directories"][search_term]
    except KeyError:
        return f"No term {search_term} in given directory"
