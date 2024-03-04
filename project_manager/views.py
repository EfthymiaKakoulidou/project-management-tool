from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView, TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from .models import Task, Profile
from .forms import ProjectForm, TaskForm, ProfileForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin)
import random
from django.db.models import Q


class Projectdetail(DetailView):
    """Creates project detail"""

    template_name = "project_manager/project_detail.html"
    model = Project
    context_object_name = "project"


class Projects(LoginRequiredMixin, ListView):
    """Create List of Projects"""

    template_name = "project_manager/projects.html"
    model = Project
    context_object_name = "projects"
    def get_queryset(self):
        return Project.objects.filter(Q(user=self.request.user) | Q(task__assigned_to=self.request.user)).distinct()


class AddProject(LoginRequiredMixin, CreateView):
    """Create project view"""

    template_name = "project_manager/add_project.html"
    model = Project
    success_url = "projects"
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.title = form.cleaned_data['title']
        project.title = form.instance.title
        return super(AddProject, self).form_valid(form)

class Tasks(LoginRequiredMixin, ListView):
    """Create List of Tasks"""
    template_name = "project_manager/my_tasks.html"
    model = Task
    context_object_name = "tasks"
    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user).order_by('deadline')


class AddTask(LoginRequiredMixin, CreateView):
    """Create task view"""

    template_name = "project_manager/add_task.html"
    model = Task
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        global project
        project_id = self.kwargs['project_id']
        project = Project.objects.get(pk=project_id)
        task = form.save(commit=False)
        task.project = project
        if task.project.deadline < task.deadline:
            messages.error(self.request, "Task deadline cannot be after project deadline.")
            return redirect('add_task', project_id=project.id)
        task.save()
        return super(AddTask, self).form_valid(form) 

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return kwargs

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': project.pk})


class EditTask(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit Task"""
    template_name = 'project_manager/edit_task.html'
    model = Task
    form_class = TaskForm

    def test_func(self):
        return self.request.user == self.get_object().user
    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.object.pk})

class DeleteTask(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete Task"""
    model = Task
    success_url = "project_manager/project_detail/"

    def test_func(self):
        return self.request.user == self.get_object().user

    def get_success_url(self):
        task = self.get_object()
        return reverse_lazy('project_detail', kwargs={'pk': task.project.pk})

class TaskDetail(DetailView):
    """Creates task detail"""

    template_name = "project_manager/task_detail.html"
    model = Task
    context_object_name = "task"

class DeleteProject(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete Project"""
    model = Project
    def test_func(self):
        return self.request.user == self.get_object().user
    def get_success_url(self):
        return reverse_lazy('projects')


class EditProject(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit Project"""
    template_name = 'project_manager/edit_project.html'
    model = Project
    success_url = "/project_detail/"
    form_class = ProjectForm
    def test_func(self):
        return self.request.user == self.get_object().user
    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.pk})

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
    context_object_name = "profile"

    def get(self, request, *args, **kwargs):
        user_profile = Profile.objects.filter(user=request.user).first()
        if user_profile:
            return redirect('profile_detail', pk=user_profile.pk)
        else:
            return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddProfile, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'pk': self.object.pk})

class DeleteProfile(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete Profile"""
    model = Profile
    def test_func(self):
        return self.request.user == self.get_object().user
    def get_success_url(self):
        return reverse_lazy('profiles')


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit Profile"""
    template_name = 'project_manager/edit_profile.html'
    model = Profile
    form_class = ProfileForm
    def test_func(self):
        return self.request.user == self.get_object().user
   
    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'pk': self.object.pk})

class Home(TemplateView):
    template_name = 'home.html'
    
    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        motivational_quotes = ['"The most certain way to succeed is always to try just one more time." - Thomas Edison.',
        "'The only way to do great work is to love what you do.' - Steve Jobs",
        '"In the middle of every difficulty lies opportunity." - Albert Einstein',
        '"The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks." - Mark Zuckerberg']
        random_motivation = random.choice(motivational_quotes)
        context['random_motivation'] = random_motivation
        return context

