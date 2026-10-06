from django.contrib import admin
from django.urls import path

from todo_app.views import (
    HomePageView,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    NoteCreateView,
    SubTaskCreateView,
)


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", HomePageView.as_view(), name="home"),

    path("tasks/", TaskListView.as_view(), name="task-list"),

    path(
        "tasks/add/",
        TaskCreateView.as_view(),
        name="task-add"
    ),

    path(
        "tasks/<int:pk>/",
        TaskDetailView.as_view(),
        name="task-detail"
    ),

    path(
        "tasks/<int:pk>/edit/",
        TaskUpdateView.as_view(),
        name="task-edit"
    ),

    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),

    path(
        "tasks/<int:task_id>/notes/add/",
        NoteCreateView.as_view(),
        name="note-add"
    ),

    path(
        "tasks/<int:task_id>/subtasks/add/",
        SubTaskCreateView.as_view(),
        name="subtask-add"
    ),
]