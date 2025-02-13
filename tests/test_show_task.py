# tests/test_show_tasks.py
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from commands import handle_show_tasks
from database import add_task, DB_NAME
import sqlite3

@pytest.fixture
def setup_database():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()
    
    yield
    
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

def test_show_tasks_empty(setup_database):
    result = handle_show_tasks()
    assert "📭 Görev listesi boş!" == result

def test_show_tasks_with_items(setup_database):
    add_task("Task 1")
    add_task("Task 2")
    
    result = handle_show_tasks()
    expected = "1. Task 1 ❌\n2. Task 2 ❌"
    assert expected == result
