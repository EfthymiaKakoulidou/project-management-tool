from django.urls import path
from .views import AddProject, Projects, Projectdetail


urlpatterns = [
    path("", AddProject.as_view(), name="add_project"),
    path("project_manager", Projects.as_view(), name="projects"),
    path("<slug:pk>", Projectdetail.as_view(), name="project_detail"),
]
