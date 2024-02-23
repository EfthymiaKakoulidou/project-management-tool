from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from .forms import ProjectForm
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

class AddProject(LoginRequiredMixin, CreateView):
    """Create project view"""
    template_name = 'project_manager/add_project.html'
    model = Project
    success_url = '/add_project'
    form_class = ProjectForm 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddProject, self).form_valid(form)
