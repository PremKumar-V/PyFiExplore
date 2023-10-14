import os
import json
from variables import load_dotenv

load_dotenv()


def save_directory_structure(directory, json_filename):
    file_list = {}

    for root, _, files in os.walk(directory):
        for file in files:
            file_list[file] = os.path.join(root, file)

    with open(json_filename, "w") as json_file:
        json.dump(file_list, json_file)


def load_directory_structure(json_filename):
    try:
        with open(json_filename, "r") as json_file:
            file_list = json.load(json_file)
        return file_list
    except FileNotFoundError:
        return None


directory_to_search = os.getenv("SEARCH_PATH")
json_filename = "directory_structure.json"

save_directory_structure(directory_to_search, json_filename)
print(f"Directory structure saved to {json_filename}")

loaded_directory = load_directory_structure(json_filename)


def find_file(file_name):
    if loaded_directory:
        if file_name in loaded_directory:
            print(f"File '{file_name}' found at: {loaded_directory[file_name]}")
        else:
            print(f"File '{file_name}' not found in the directory structure.")
    else:
        print(f"Error: JSON file '{file_name}' not found.")


find_file("Abc.jpeg")
