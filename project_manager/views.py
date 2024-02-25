from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from .models import Task
from .forms import ProjectForm, TaskForm
from django.shortcuts import render

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin)

def index(request):
    return render(request, "index.html")


class Projectdetail(DetailView):
    """Creates project detail"""

    template_name = "project_manager/project_detail.html"
    model = Project
    context_object_name = "project"


class Projects(ListView):
    """Create List of Projects"""

    template_name = "project_manager/projects.html"
    model = Project
    context_object_name = "projects"


class AddProject(LoginRequiredMixin, CreateView):
    """Create project view"""

    template_name = "project_manager/add_project.html"
    model = Project
    success_url = "/project_manager"
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddProject, self).form_valid(form)

class AddTask(LoginRequiredMixin, CreateView):
    """Create task view"""

    template_name = "project_manager/add_task.html"
    model = Task
    success_url = "/project_detail"
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddTask, self).form_valid(form)

class DeleteProject(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete Project"""
    model = Project
    success_url = "/project_manager/"
    def test_func(self):
        return self.request.user == self.get_object().owner


class EditProject(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit Project"""
    template_name = 'project_manager/edit_project.html'
    model = Project
    success_url = "/project_manager/"
    form_class = ProjectForm
    def test_func(self):
        return self.request.user == self.get_object().owner


class MyProfile(ListView):
    """Profiles"""
    template_name = "project_manager/my_profile.html"
    model = Project
    