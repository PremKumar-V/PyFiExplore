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
        sub_dirs,
        files,
    ) in os.walk(search_file_path):
        dir_name = dir.split("\\")[-1]

        cur.execute(
            f"""
            INSERT INTO FILE_SYSTEM (name, path, is_folder) VALUES ('{dir_name}', '{dir}', true )
            """
        )
        for sub_dir in sub_dirs:
            sub_dir_name = sub_dir.split("\\")[-1]
            cur.execute(
                f"""
                    INSERT INTO FILE_SYSTEM (name, path, is_folder) VALUES ('{sub_dir_name}', '{sub_dir}', true )
                    """
            )
        if files:
            for file in files:
                file_name = os.path.splitext(file)[0]
                cur.execute(
                    f"""
                    INSERT INTO FILE_SYSTEM (name, path, is_folder) VALUES ('{file_name}', '{file}', false )
                    """
                )

        conn.commit()
    conn.close()


insert_in_database()
