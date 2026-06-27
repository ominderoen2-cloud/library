from database.database import create_table
import psycopg2
import os 
import database as db
from app import app
import pytest
TEST_DB = "test_connect.db"
@pytest.fixture
def client():
    app.config["TESTING "] = True
    def test_connect_db():
        return psycopg2.connect(TEST_DB)
    db.connect_db = test_connect_db
    if os.psth.exists(TEST_DB):
        os.remove(TEST_DB)
    create_table()
    with app.test_client() as client:
        yield client
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    
