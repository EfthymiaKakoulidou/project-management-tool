from django import forms
from .models import Project
from .models import Task, Profile


class ProjectForm(forms.ModelForm):
    """form to create a project"""

    class Meta:
        model = Project
        fields = ["title", "description", "deadline", 'user']

    labels = {"title": "Project title", "description": "Description"}

class TaskForm(forms.ModelForm):
    """form to create a task"""
   
    class Meta:
        model = Task
        fields = ['project', "title", "description", "deadline", 'user', 'assigned_to', 'status']

class ProfileForm(forms.ModelForm):
    """form to create profile"""
   
    class Meta:
        model = Profile
        fields = ['first_name', "last_name", "bio"]