from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from todo_app.views import (
    HomePageView,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    NoteCreateView,
    SubTaskCreateView,
    SignUpView,
)


urlpatterns = [
    path("admin/", admin.site.urls),

    # Main pages
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

    # Authentication
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login"
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),

    # Sign up
    path(
        "signup/",
        SignUpView.as_view(),
        name="signup"
    ),

    path("accounts/", include("allauth.urls")),

    # Password reset
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="registration/password_reset.html"
        ),
        name="password-reset"
    ),

    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="registration/password_reset_done.html"
        ),
        name="password-reset-done"
    ),

    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html"
        ),
        name="password-reset-confirm"
    ),

    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_complete.html"
        ),
        name="password-reset-complete"
    ),
]