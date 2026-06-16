import sqlite3

class todoDatabase:
    def __init__(self, db_name="todo.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    
    def create_table(self):
        #creates table with task id and task text
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                task_text TEXT NOT NULL
                                )
                                """)
        self.conn.commit()
      
        
    def insert_task(self, task):
        #adds a new task into database, returns task ID
        self.cursor.execute("INSERT INTO tasks (task_text) VALUES(?)", (task,))
        self.conn.commit()
        return self.cursor.lastrowid
         
    
    def remove_task(self, task_id):
        #removes a task from the database via ID
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()
        
        
    def fetch_tasks(self):
        #returns tasks as tuples (id, task_text)
        self.cursor.execute("SELECT id, task_text FROM tasks")
        return self.cursor.fetchall()