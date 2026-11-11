import pytest

from palm.db import init_db
from palm.fees import get_student_balance


@pytest.fixture(autouse=True)
def demo_db(tmp_path, monkeypatch):
    """Give every test its own fresh database, found through PALM_DB_PATH."""
    path = tmp_path / "palm_test.db"
    monkeypatch.setenv("PALM_DB_PATH", str(path))
    init_db()
    return path


def test_known_student_balance():
    assert get_student_balance("amina@palm.edu") == 1200.00


def test_student_with_zero_balance():
    assert get_student_balance("kwame@palm.edu") == 0.00


def test_unknown_student_returns_none():
    assert get_student_balance("nobody@palm.edu") is None


def test_sql_injection_does_not_leak_another_balance():
    # Bug 3 from the seminar: with an f-string query this input
    # would return another student's balance.
    assert get_student_balance("' OR '1'='1' --") is None
