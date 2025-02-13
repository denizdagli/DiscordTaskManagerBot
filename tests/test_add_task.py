# tests/test_add_task.py
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from commands import handle_add_task
from database import add_task, show_tasks, DB_NAME
import sqlite3

@pytest.fixture
def setup_database():
    # Create a test database
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
    
    # Cleanup after tests
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

def test_add_task_success(setup_database):
    # Test adding a task
    result = handle_add_task(["Buy", "milk"])
    assert "✅ Görev eklendi: Buy milk" == result
    
    # Verify task was added to database
    tasks = show_tasks()
    assert len(tasks) == 1
    assert tasks[0][1] == "Buy milk"
    assert tasks[0][2] == 0  # Not completed

def test_add_task_empty_description(setup_database):
    result = handle_add_task([])
    assert "Lütfen bir görev açıklaması girin!" == result