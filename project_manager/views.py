from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView, TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from .models import Task, Profile, ProjectsTasksMixin
from .forms import ProjectForm, TaskForm, ProfileForm, TaskFormStatus, SearchForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin)
import random
from django.db.models import Q
from django.db.models import Count


class Projectdetail(ProjectsTasksMixin, DetailView):
    """Creates project detail"""

    template_name = "project_manager/project_detail.html"
    model = Project
    context_object_name = "project"
  

class Projects(ProjectsTasksMixin, LoginRequiredMixin, ListView):
    """Create List of Projects"""

    template_name = "project_manager/projects.html"
    model = Project
    context_object_name = "projects"
    def get_queryset(self):
        return Project.objects.filter(Q(user=self.request.user) | Q(task__assigned_to=self.request.user)).distinct()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = context['projects']
        projects_with_done_task_count = projects.annotate(done_task_count=Count('task', filter=Q(task__status="Done")))
        context['projects'] = projects_with_done_task_count
        return context
  
class AddProject(ProjectsTasksMixin, LoginRequiredMixin, CreateView):
    """Create project view"""

    template_name = "project_manager/add_project.html"
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        project = form.save()
        messages.success(self.request, "Project successfully added.")
        return super(AddProject, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.pk})

class Tasks(ProjectsTasksMixin, LoginRequiredMixin, ListView):
    """Create List of Tasks"""
    template_name = "project_manager/my_tasks.html"
    model = Task
    context_object_name = "tasks"
    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user).order_by('deadline')

class AddTask(ProjectsTasksMixin, LoginRequiredMixin, CreateView):
    """Create task view"""
    template_name = "project_manager/add_task.html"
    model = Task
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        project_id = self.kwargs['project_id']
        project = get_object_or_404(Project, pk=project_id)
        form.instance.project = project

        if project.deadline < form.instance.deadline:
            messages.error(self.request, "Task deadline cannot be after project deadline.")
            return redirect('add_task', project_id=project.id)

        response = super().form_valid(form)

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = self.kwargs.get('project_id')
        context['project'] = get_object_or_404(Project, pk=project_id)
        return context

    def get_success_url(self):
        messages.success(self.request, "Task successfully added.")
        project_pk = self.object.project.pk
        return reverse_lazy('project_detail', kwargs={'pk': project_pk})


class EditTask(ProjectsTasksMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit Task"""
    template_name = 'project_manager/edit_task.html'
    model = Task
    form_class = TaskForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_id = self.object.pk
        task = get_object_or_404(Task, pk=task_id)
        context['project'] = get_object_or_404(Project, pk=task.project.id)
        return context
    def test_func(self):
        task = self.get_object()
        return self.request.user == task.user
    def get_success_url(self):
        messages.success(self.request, "Task successfully edited.")
        return reverse_lazy('edit_task_status', kwargs={'pk': self.object.pk})


class EditTaskStatus(ProjectsTasksMixin, UpdateView):
    model = Task
    form_class = TaskFormStatus
    template_name = 'project_manager/edit_task_status.html'

    def get_success_url(self):
        messages.success(self.request, "Status successfully updated.")
        return reverse_lazy('edit_task_status', kwargs={'pk': self.object.pk})

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.user or self.request.user == task.assigned_to

class DeleteTask(ProjectsTasksMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete Task"""
    model = Task
    success_url = "project_manager/project_detail/"

    def test_func(self):
        return self.request.user == self.get_object().user

    def get_success_url(self):
        task = self.get_object()
        messages.success(self.request, "Task successfully deleted.")
        return reverse_lazy('project_detail', kwargs={'pk': task.project.pk})

class DeleteProject(ProjectsTasksMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete Project"""
    model = Project
    def test_func(self):
        return self.request.user == self.get_object().user
    def get_success_url(self):
        messages.success(self.request, "Project successfully deleted.")
        return reverse_lazy('projects')


class EditProject(ProjectsTasksMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit Project"""
    template_name = 'project_manager/edit_project.html'
    model = Project
    success_url = "/project_detail/"
    form_class = ProjectForm
    def test_func(self):
        return self.request.user == self.get_object().user
    def get_success_url(self):
        messages.success(self.request, "Project successfully edited.")
        return reverse_lazy('project_detail', kwargs={'pk': self.object.pk})

class ProfileDetail(ProjectsTasksMixin, DetailView):
    """Creates profile detail"""

    template_name = "project_manager/profile_detail.html"
    model = Profile
    context_object_name = "profile"


class Profiles(ProjectsTasksMixin, ListView):
    """Create List of Projects"""

    template_name = "project_manager/profiles.html"
    model = Profile
    context_object_name = "profiles"

    
class AddProfile(ProjectsTasksMixin, LoginRequiredMixin, CreateView):
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
        messages.success(self.request, "Profile successfully added.")
        return reverse_lazy('profile_detail', kwargs={'pk': self.object.pk})

class DeleteProfile(ProjectsTasksMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete Profile"""
    model = Profile
    def test_func(self):
        return self.request.user == self.get_object().user
    def get_success_url(self):
        messages.success(self.request, "Profile successfully deleted.")
        return reverse_lazy('profiles')


class EditProfile(ProjectsTasksMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit Profile"""
    template_name = 'project_manager/edit_profile.html'
    model = Profile
    form_class = ProfileForm
    def test_func(self):
        return self.request.user == self.get_object().user
   
    def get_success_url(self):
        messages.success(self.request, "Profile successfully edited.")
        return reverse_lazy('profile_detail', kwargs={'pk': self.object.pk})


class Home(TemplateView):
    template_name = 'project_manager/home.html'
    
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

from django.shortcuts import render
from .forms import SearchForm

def search_results_view(request):
    form = SearchForm(request.GET)
    context = {
        'form': form
    }
    return render(request, 'search_results.html', context)