import os
from sqlite3 import OperationalError
from dotenv import load_dotenv
from db.database import init_database

load_dotenv()
search_file_path = os.getenv("SEARCH_PATH")


def insert_in_database():
    conn, cur = init_database()

    for (
        dir,
        _,
        files,
    ) in os.walk(search_file_path):
        dir_name = dir.split("\\")[-1]
        # file_name = os.path.splitext(files)[0]
        cur.execute(
            f"""
            INSERT INTO FILE_SYSTEM (name, path, is_folder) VALUES (
            '{dir_name}',
            '{dir}',
            true
            )
            """
        )
        conn.commit()
        break
    conn.close()


insert_in_database()
