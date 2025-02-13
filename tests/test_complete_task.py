# tests/test_complete_task.py
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from commands import handle_complete_task
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

def test_complete_task_success(setup_database):
    result = handle_complete_task(["1"])
    assert "✅ Görev tamamlandı: 1" == result
    
    # Verify task was marked as completed
    tasks = show_tasks()
    assert tasks[0][2] == 1  # Completed

def test_complete_task_invalid_id(setup_database):
    result = handle_complete_task([])
    assert "Lütfen geçerli bir görev ID'si girin!" == result
    
    result = handle_complete_task(["abc"])
    assert "Lütfen geçerli bir görev ID'si girin!" == result