from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    """form to create a project"""

    class Meta:
        model = Project
        fields = ["title", "description", "deadline", "owner"]

    labels = {"title": "Project title", "description": "Description"}
