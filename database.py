import sqlite3

# Veritabanı bağlantısını oluştur
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Tasks tablosunu oluştur
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    status TEXT CHECK (status IN ('pending', 'completed')) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

# Görev ekleme
def add_task(description):
    cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
    conn.commit()
    return f"Görev eklendi: {description}"

# Görev silme
def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    return f"Görev silindi: ID {task_id}"

# Tüm görevleri listeleme
async def task_list():
    conn = sqlite3.connect("tasks.db")  # Veritabanına bağlan
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    
    conn.close()  # Veritabanını kapat
    
    if not tasks:
        return "Henüz eklenmiş bir görev yok."

    task_messages = [f"**ID:** {task[0]}, **Açıklama:** {task[1]}, **Durum:** {task[2]}, **Tarih:** {task[3]}" for task in tasks]
    
    return "\n".join(task_messages)

# Görevi tamamlandı olarak işaretleme
def complete_task(task_id):
    cursor.execute("UPDATE tasks SET status = 'completed' WHERE id = ?", (task_id,))
    conn.commit()
    return f"Görev tamamlandı olarak işaretlendi: ID {task_id}"



# Bağlantıyı kapat
conn.close()
