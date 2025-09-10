import pytest
from django.test import Client

client = Client()

@pytest.mark.django_db
def test_create_task():
    response = client.post(
        "/tasks/",
        data={
            "title": "Test Task",
            "description": "Testing",
            "due_date": "2025-09-15",
            "status": "Pending",
        },
        content_type="application/json",
    )
    assert response.status_code == 201

@pytest.mark.django_db
def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.django_db
def test_update_task():
    # First create task
    create_res = client.post(
        "/tasks/",
        data={"title": "Temp Task", "description": "", "due_date": "2025-09-12", "status": "Pending"},
        content_type="application/json",
    )
    task_id = client.get("/tasks/").json()[0]["id"]

    update_res = client.put(
        f"/tasks/{task_id}/",
        data={"title": "Updated Task", "description": "Updated desc", "due_date": "2025-09-13", "status": "Done"},
        content_type="application/json",
    )
    assert update_res.status_code == 200

@pytest.mark.django_db
def test_delete_task():
    # Create task
    client.post(
        "/tasks/",
        data={"title": "Delete Me", "description": "", "due_date": "2025-09-12", "status": "Pending"},
        content_type="application/json",
    )
    task_id = client.get("/tasks/").json()[0]["id"]

    delete_res = client.delete(f"/tasks/{task_id}/")
    assert delete_res.status_code == 200
