import mysql.connector
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MySQL config
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    # "password": "your_password",
    "database": "todo_list",
    "raise_on_warnings": True,
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def execute_query(query, params=(), fetchone=False, fetchall=False, return_lastrowid=False):
    conn, cursor = None, None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)

        if fetchone:
            row = cursor.fetchone()
            return row
        if fetchall:
            rows = cursor.fetchall()
            return rows
        if return_lastrowid:
            conn.commit()
            return cursor.lastrowid

        conn.commit()
    except mysql.connector.Error as e:
        logger.exception("Database error: %s", e)
        raise
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def init_db():
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT,
        due_date DATE,
        status VARCHAR(50)
    );
    """
    execute_query(create_table_sql)
    logger.info("Tasks table initialized.")

# CRUD functions
def create_task(title, description, due_date, status):
    try:
        new_id = execute_query(
            "INSERT INTO tasks (title, description, due_date, status) VALUES (%s, %s, %s, %s)",
            (title, description, due_date, status),
            return_lastrowid=True
        )
        logger.info(f"Task created: {title}")
        return get_task(new_id) 
    except Exception as e:
        logger.error(f"Error creating task: {e}")
        raise

def get_all_tasks():
    try:
        rows = execute_query(
            "SELECT id, title, description, due_date, status FROM tasks ORDER BY id DESC",
            fetchall=True
        )
        return [
            {"id": r[0], "title": r[1], "description": r[2],
             "due_date": r[3].isoformat() if r[3] else None,
             "status": r[4]} for r in rows
        ]
    except Exception as e:
        logger.error(f"Error fetching tasks: {e}")
        raise

def get_task(task_id):
    try:
        r = execute_query(
            "SELECT id, title, description, due_date, status FROM tasks WHERE id=%s",
            (task_id,),
            fetchone=True
        )
        if not r:
            return None
        return {"id": r[0], "title": r[1], "description": r[2],
                "due_date": r[3].isoformat() if r[3] else None,
                "status": r[4]}
    except Exception as e:
        logger.error(f"Error fetching task {task_id}: {e}")
        raise

def update_task(task_id, title, description, due_date, status):
    try:
        execute_query(
            "UPDATE tasks SET title=%s, description=%s, due_date=%s, status=%s WHERE id=%s",
            (title, description, due_date, status, task_id)
        )
        logger.info(f"Task updated: {task_id}")
        return get_task(task_id) 
    except Exception as e:
        logger.error(f"Error updating task {task_id}: {e}")
        raise

def delete_task(task_id):
    try:
        execute_query("DELETE FROM tasks WHERE id=%s", (task_id,))
        logger.info(f"Task deleted: {task_id}")
    except Exception as e:
        logger.error(f"Error deleting task {task_id}: {e}")
        raise
