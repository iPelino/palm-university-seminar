"""Create and seed the demo SQLite database.

Run:  python -m palm.db
The database path comes from the PALM_DB_PATH environment variable
(default: palm.db in the current folder). Never hardcode a personal path.
"""
import os
import sqlite3

SEED_STUDENTS = [
    ("amina@palm.edu", 1200.00),
    ("kwame@palm.edu", 0.00),
    ("zawadi@palm.edu", 450.50),
]


def get_db_path() -> str:
    """Return the database path from the environment."""
    return os.environ.get("PALM_DB_PATH", "palm.db")


def init_db(path: str | None = None) -> str:
    """Create the fees table and insert the seed students. Returns the path used."""
    path = path or get_db_path()
    with sqlite3.connect(path) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS fees ("
            "email TEXT PRIMARY KEY, "
            "balance REAL NOT NULL)"
        )
        conn.executemany(
            "INSERT OR REPLACE INTO fees (email, balance) VALUES (?, ?)",
            SEED_STUDENTS,
        )
    return path


if __name__ == "__main__":
    print(f"Database ready at {init_db()}")
