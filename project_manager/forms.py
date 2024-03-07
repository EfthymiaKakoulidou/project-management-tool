from django import forms
from .models import Project
from .models import Task, Profile


class ProjectForm(forms.ModelForm):
    """form to create a project"""

    class Meta:
        model = Project
        fields = ["title", "description", "deadline"]
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }

    labels = {"title": "Project title", "description": "Description"}

class TaskForm(forms.ModelForm):
    """form to create a task"""
   
    class Meta:
        model = Task
        fields = ["title", "description", "deadline", 'assigned_to', 'status']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }

class TaskFormAT(forms.ModelForm):
    """form with just status field"""
   
    class Meta:
        model = Task
        fields = ['status']


class ProfileForm(forms.ModelForm):
    """form to create profile"""
   
    class Meta:
        model = Profile
        fields = ['first_name', "last_name",'featured_image', 'job_title', "bio"]