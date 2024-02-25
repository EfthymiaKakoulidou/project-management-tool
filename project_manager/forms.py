from django import forms
from .models import Project
from .models import Task


class ProjectForm(forms.ModelForm):
    """form to create a project"""

    class Meta:
        model = Project
        fields = ["title", "description", "deadline"]

    labels = {"title": "Project title", "description": "Description"}

class TaskForm(forms.ModelForm):
    """form to create a task"""
   
    class Meta:
        model = Task
        fields = ['project', "title", "description", "deadline", 'owner', 'owned_by', 'status']

 