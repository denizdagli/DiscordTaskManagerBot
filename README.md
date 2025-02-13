# TaskBot - Discord Task Management Bot

TaskBot is a simple and easy-to-use Discord bot for managing tasks in your server. It allows users to add tasks, delete tasks, mark tasks as completed, and view all tasks in a neat list. Tasks are stored in a SQLite database.

## Features

- ✨ Add tasks with descriptions.  
- 🗑️ Remove tasks by their ID. 
- ✅ Mark tasks as completed.
- 📝 List all tasks with their completion status.
- 💾 Persistent storage using SQLite database
- 🧪 Comprehensive test coverage

## Installation

### Requirements

- **Python 3.6+**  
- **SQLite** (bundled with Python by default)  
- **discord.py** (Python library for interacting with Discord)
- **dotenv** (for handling environment variables)

### Steps to Install

1. Clone the repository:
   
   ```bash
   git clone https://github.com/yourusername/taskbot.git
   cd taskbot

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

3. Create a .env file in the root directory of the project and add your Discord bot token:
    ```bash
    DISCORD_TOKEN=your_bot_token

4. Create the database and initialize the bot:
    ```bash
    python database.py

5. Run the bot:
    ```bash
    python bot.py

Now, the bot will be running and ready to interact with users on your server!

## Available Commands

* ``!add <task description>``: Adds a new task to the list.
_Example_: ``!add Buy groceries``

* ``!delete <task ID>``: Deletes a task by its ID.
_Example_: ``!delete 1``

* !show: Displays a list of all tasks.
_Example_: 
````
1. Buy groceries ❌
2. Complete project ✅

````
* ``!complete <task ID>``: Marks a task as completed by its ID.
_Example_: ``!complete 1``


## File Structure
```bash
taskbot/
│
├── bot.py                 # Bot file that runs the bot
├── database.py            # SQLite database operations
├── commands.py            # Command handling functions
├── .env                   # Discord token for bot authentication
├── requirements.txt       # Required Python dependencies
└── README.md              # This file
└── tests/                 # Test folder
    ├── __init__.py        # This file makes the tests/ folder a Python package
    ├── test_add_task.py   
    └── test_complete_task.py   
    └── test_delete_task.py   
    └── test_show_task.py   


## Testing
```bash
pytest tests/

## Contributing

1. Fork the repository
2. Create a new branch: ``git checkout -b feature-name``
3. Make your changes and commit:`` git commit -m 'Add some feature'``
4. Push to the branch: ``git push origin feature-name``
5. Submit a pull request


### And
Thanks to the Discord.py team for their excellent library