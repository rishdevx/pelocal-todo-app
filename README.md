# Pelocal To-Do List Application

A Python Django-based To-Do List application with RESTful APIs and web templates for managing tasks. Uses MySQL as the database (no ORM) and raw SQL queries for database operations.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Web Interface](#web-interface)
- [Testing](#testing)
- [Notes](#notes)

## Features
- CRUD operations on tasks (Create, Read, Update, Delete) via API
- Partial update using PATCH and full update using PUT
- **Web templates:** Display all tasks, Add new tasks via form
- MySQL database integration (no ORM, raw SQL queries)
- Logging and exception handling
- Fully tested API endpoints with pytest

## Tech Stack
- Python 3.9+
- Django 4.x
- MySQL
- mysql-connector-python for database connection
- HTML templates for UI
- pytest for testing

## Setup Instructions

1. Clone the repository
```bash
git clone pelocal
cd pelocal

# Setup Instructions:

1. Clone the repository:
```bash
git clone pelocal
cd pelocal
```

2. Create virtual environment & activate:
```bash
python3 -m venv env
source env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure MySQL database:
```sql
CREATE DATABASE todo_list;
```

5. Update tasks/db.py with your MySQL credentials:
```sql
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "<your_password>",
    "database": "todo_list",
}
```

6. Initialize database:
```bash
python manage.py shell
>>> from tasks import db
>>> db.init_db()
>>> exit()
```

## Running the Application 
```bash
python manage.py runserver
Web UI: http://127.0.0.1:8000/
```

**-----------------**

## API Endpoints

# Base URL
http://localhost:8000/


# Endpoints

1. # Description: Retrieve a list of all tasks.
GET /tasks/

**Response:**
```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, Bread, Eggs",
    "due_date": "2025-09-15",
    "status": "Pending"
  },
  {
    "id": 2,
    "title": "Walk the dog",
    "description": "",
    "due_date": null,
    "status": "Completed"
  }
]
```

# Status Codes:  
200 OK – Success


**----------------------**


2. # Description: Retrieve a task by ID
GET /tasks/<int:task_id>/

**Response:**
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs",
  "due_date": "2025-09-15",
  "status": "Pending"
}
```

# Status Codes:
200 OK – Success
404 Not Found – Task ID does not exist


**----------------------**


3. # Description: Create a new task.
POST /tasks/

# Request Body (JSON):
```json
{
  "title": "New Task",
  "description": "Description of task",
  "due_date": "2025-09-20",
  "status": "Pending"
}
```

# Response (example):
```json
{
  "message": "Task created"
}
```

# Status Codes:
201 Created – Task successfully created
400 Bad Request – Title is missing 


**----------------------**


4. # Description: Fully update a task. All fields are required.
PUT /tasks/<int:task_id>/

# Request Body (JSON):
```json
{
  "title": "Updated Task",
  "description": "Updated description",
  "due_date": "2025-09-25",
  "status": "Completed"
}
```

# Response:
```json
{
  "message": "Task updated"
}
```

# Status Codes:
200 OK – Task updated successfully
404 Not Found – Task does not exist


**----------------------**


4. # Description: Partially update a task. Only provide fields you want to update.
PATCH /tasks/<int:task_id>/

# Request Body (JSON):
```json
{
  "title": "Partial Update",
  "status": "Completed"
}
```

# Response:
```json
{
  "message": "Task updated"
}
```


# Status Codes:
200 OK – Task updated successfully
404 Not Found – Task does not exist


**----------------------**


6. # Description: Delete a task by ID.
DELETE /tasks/<int:task_id>/

# Response:
```json
{
  "message": "Task deleted"
}
```

# Status Codes:
200 OK – Task deleted successfully
404 Not Found – Task does not exist


# Api Notes:
Content-Type: All request bodies must be application/json.
CSRF: API views are exempted from CSRF (@csrf_exempt).

Task Fields:
title (string, required)
description (string, optional)
due_date (YYYY-MM-DD, optional)
status (Pending or Completed)


## Testing
Ensure you are in the virtual environment:
```bash
pytest -v
```

Tests include:
Create task
Get all tasks
Update task (PUT & PATCH)
Delete task

# Notes
No ORM used — all database operations are raw SQL in tasks/db.py
Logging is enabled in db.py for database operations
CSRF protection is disabled in API views for simplicity (@csrf_exempt)
UI templates are in tasks/templates/