"""Tuition balance lookup.

This is the correct version of the PR #14 code from the seminar slides:
- keeps the agreed name get_student_balance
- reads the database path from PALM_DB_PATH
- uses a ? placeholder, so user input is never pasted into SQL
"""
import sqlite3

from palm.db import get_db_path


def get_student_balance(email: str) -> float | None:
    """Return the tuition balance for a student, or None if the email is unknown."""
    with sqlite3.connect(get_db_path()) as conn:
        row = conn.execute(
            "SELECT balance FROM fees WHERE email = ?",
            (email,),
        ).fetchone()
    return row[0] if row else None
