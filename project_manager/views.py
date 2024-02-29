from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from .models import Task, Profile
from .forms import ProjectForm, TaskForm, ProfileForm
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


class Tasks(ListView):
    """Create List of Projects"""
    template_name = "project_manager/projects.html"
    model = Task
    context_object_name = "task"


class AddTask(LoginRequiredMixin, CreateView):
    """Create task view"""

    template_name = "project_manager/add_task.html"
    model = Task
    success_url = "/<slug:pk>/"
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddTask, self).form_valid(form)

class EditTask(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit Task"""
    template_name = 'project_manager/edit_task.html'
    model = Task
    success_url = "/project_manager/"
    form_class = TaskForm
    def test_func(self):
        return self.request.user == self.get_object().user

class DeleteTask(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete Task"""
    model = Task
    success_url = "/project_manager/"
    def test_func(self):
        return self.request.user == self.get_object().user

class TaskDetail(DetailView):
    """Creates task detail"""

    template_name = "project_manager/task_detail.html"
    model = Task
    context_object_name = "task"

class DeleteProject(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete Project"""
    model = Project
    success_url = "/project_manager/"
    def test_func(self):
        return self.request.user == self.get_object().user


class EditProject(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit Project"""
    template_name = 'project_manager/edit_project.html'
    model = Project
    success_url = "/project_manager/"
    form_class = ProjectForm
    def test_func(self):
        return self.request.user == self.get_object().user

class ProfileDetail(DetailView):
    """Creates profile detail"""

    template_name = "project_manager/profile_detail.html"
    model = Profile
    context_object_name = "profile"



class Profiles(ListView):
    """Create List of Projects"""

    template_name = "project_manager/profiles.html"
    model = Profile
    context_object_name = "profiles"


class AddProfile(LoginRequiredMixin, CreateView):
    """Profiles"""
    template_name = "project_manager/add_profile.html"
    model = Profile
    form_class = ProfileForm
    success_url = "/project_manager/"
    context_object_name = "profile"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddProfile, self).form_valid(form)

class DeleteProfile(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete Profile"""
    model = Profile
    success_url = "/project_manager/"
    def test_func(self):
        return self.request.user == self.get_object().user


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit Profile"""
    template_name = 'project_manager/edit_profile.html'
    model = Profile
    success_url = "/project_manager/"
    form_class = ProfileForm
    def test_func(self):
        return self.request.user == self.get_object().user
       