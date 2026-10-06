from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView

from .models import Task, Note, SubTask
from .forms import TaskForm, NoteForm, SubTaskForm


class HomePageView(ListView):
    model = Task
    template_name = "home.html"
    context_object_name = "tasks"
    ordering = ["deadline"]


class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"
    ordering = ["deadline"]


class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = "task"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task-list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("task-list")


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "note_form.html"

    def form_valid(self, form):
        form.instance.task_id = self.kwargs["task_id"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "task-detail",
            kwargs={"pk": self.kwargs["task_id"]}
        )


class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = "subtask_form.html"

    def form_valid(self, form):
        form.instance.task_id = self.kwargs["task_id"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "task-detail",
            kwargs={"pk": self.kwargs["task_id"]}
        )


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response