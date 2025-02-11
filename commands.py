from database import add_task, delete_task, show_tasks, complete_task

def handle_add_task(args):
    if not args:
        return "Lütfen bir görev açıklaması girin!"
    description = " ".join(args)
    add_task(description)
    return f"✅ Görev eklendi: {description}"

def handle_delete_task(args):
    if not args or not args[0].isdigit():
        return "Lütfen geçerli bir görev ID'si girin!"
    delete_task(int(args[0]))
    return f"🗑️ Görev silindi: {args[0]}"

def handle_show_tasks():
    tasks = show_tasks()
    if not tasks:
        return "📭 Görev listesi boş!"
    return "\n".join([f"{t[0]}. {t[1]} {'✅' if t[2] else '❌'}" for t in tasks])

def handle_complete_task(args):
    if not args or not args[0].isdigit():
        return "Lütfen geçerli bir görev ID'si girin!"
    complete_task(int(args[0]))
    return f"✅ Görev tamamlandı: {args[0]}"
