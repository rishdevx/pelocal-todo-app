from django.urls import path
from . import views

urlpatterns = [
    # API endpoints
    path('tasks/', views.tasks_api),                  # GET all, POST
    path('tasks/<int:task_id>/', views.tasks_api),    # GET, PUT, PATCH, DELETE

    # Web views
    path("", views.task_list_view, name="index"),     
    path("tasks/add/", views.task_add_view, name="task_add"),
]
