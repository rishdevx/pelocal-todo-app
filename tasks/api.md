# API Documentation

## Base URL
http://localhost:8000/


## Endpoints

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


**----------------------**


# Notes:

**Content-Type:** All request bodies must be application/json.

**CSRF:** API views are exempted from CSRF (@csrf_exempt).

# Task Fields:

**title** (string, required)

**description** (string, optional)

**due_date** (YYYY-MM-DD, optional)

**status** (Pending or Completed)