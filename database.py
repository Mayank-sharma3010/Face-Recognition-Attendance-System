import sqlite3

def create_database():

    conn = sqlite3.connect("database/attendance.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        roll_no TEXT UNIQUE,

        branch TEXT,

        semester TEXT
    )
    """)

    conn.commit()

    conn.close()

    print("Database Created Successfully")


if __name__ == "__main__":

    create_database()