import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import db
from django.shortcuts import render, redirect


@csrf_exempt
def tasks_api(request, task_id=None):
    """
    Handles all task API requests:
    - GET /tasks/          -> list all tasks
    - POST /tasks/         -> create a task
    - GET /tasks/<id>/     -> retrieve single task
    - PUT /tasks/<id>/     -> fully update task
    - PATCH /tasks/<id>/   -> partially update task
    - DELETE /tasks/<id>/  -> delete task
    """
    try:
        if request.method == "GET":
            if task_id:
                task = db.get_task(task_id)
                if not task:
                    return JsonResponse({"error": "Task not found"}, status=404)
                return JsonResponse(task)
            else:
                tasks = db.get_all_tasks()
                return JsonResponse(tasks, safe=False)

        elif request.method == "POST" and not task_id:
            data = json.loads(request.body)
            title = data.get("title")
            if not title:
                return JsonResponse({"error": "Title is required"}, status=400)
            db.create_task(
                title,
                data.get("description", ""),
                data.get("due_date"),
                data.get("status", "Pending")
            )
            return JsonResponse({"message": "Task created"}, status=201)

        elif request.method == "PUT" and task_id:
            data = json.loads(request.body)
            title = data.get("title")
            if not title:
                return JsonResponse({"error": "Title is required"}, status=400)
            db.update_task(
                task_id,
                title,
                data.get("description", ""),
                data.get("due_date"),
                data.get("status", "Pending")
            )
            return JsonResponse({"message": "Task updated"})

        elif request.method == "PATCH" and task_id:
            data = json.loads(request.body)
            task = db.get_task(task_id)
            if not task:
                return JsonResponse({"error": "Task not found"}, status=404)

            title = data.get("title", task["title"])
            description = data.get("description", task["description"])
            due_date = data.get("due_date", task["due_date"])
            status = data.get("status", task["status"])

            db.update_task(task_id, title, description, due_date, status)
            return JsonResponse({"message": "Task updated"})

        elif request.method == "DELETE" and task_id:
            db.delete_task(task_id)
            return JsonResponse({"message": "Task deleted"})

        else:
            return JsonResponse({"error": "Method not allowed"}, status=405)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)



def task_list_view(request):
    tasks = db.get_all_tasks()
    return render(request, "index.html", {"tasks": tasks})


def task_add_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description", "")
        due_date = request.POST.get("due_date")
        status = request.POST.get("status", "Pending")

        db.create_task(title, description, due_date, status)
        return redirect("index")

    return render(request, "tasks.html")
