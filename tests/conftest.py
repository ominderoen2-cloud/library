import pytest
from database.database import connect_db
from app import app
@pytest.fixture
def client():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM borrowbooks")
    cursor.execute("DELETE FROM books")
    cursor.execute("DELETE FROM members")
    conn.commit()
    conn.close()

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client