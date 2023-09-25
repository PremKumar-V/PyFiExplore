try:
    from database import init_database
except ImportError:
    print("Error in Importing")

conn, cur = init_database()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS FILE_SYSTEM (
        id INTEGER PRIMARY KEY,
        name TEXT,
        path TEXT,
        is_folder BOOLEAN
    )
"""
)

conn.commit()
conn.close()
