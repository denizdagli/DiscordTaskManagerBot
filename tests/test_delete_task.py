# tests/test_delete_task.py
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from commands import handle_delete_task
from database import add_task, show_tasks, DB_NAME
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
    
    # Add a test task
    add_task("Test Task")
    
    yield
    
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

def test_delete_task_success(setup_database):
    result = handle_delete_task(["1"])
    assert "🗑️ Görev silindi: 1" == result
    
    # Verify task was deleted
    tasks = show_tasks()
    assert len(tasks) == 0

def test_delete_task_invalid_id(setup_database):
    result = handle_delete_task([])
    assert "Lütfen geçerli bir görev ID'si girin!" == result
    
    result = handle_delete_task(["abc"])
    assert "Lütfen geçerli bir görev ID'si girin!" == result
