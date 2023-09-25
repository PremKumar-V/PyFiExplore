import os
import sqlite3
from dotenv import load_dotenv

env_variable = load_dotenv()

def init_database():
    path = os.getenv('DATABASE_PATH')
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    return connection, cursor