import pytest
import sqlite3


@pytest.fixture(scope='function')
def db_connection():
    connection = sqlite3.connect(':Память:')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE records (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')

    connection.commit()
    yield connection  
    connection.close()