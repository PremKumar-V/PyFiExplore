from dotenv import load_dotenv
import os


class Variable:
    def __init__(self) -> None:
        load_dotenv()

        self.search_path = os.getenv("SEARCH_PATH")
        self.data_file_path = os.getenv("DATA_FILE_PATH")
