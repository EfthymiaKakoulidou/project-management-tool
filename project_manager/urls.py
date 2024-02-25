from django.urls import path
from .views import (
    AddProject, Projects, Projectdetail, 
    DeleteProject, EditProject, MyProfile, AddTask
)

urlpatterns = [
    path("add_project", AddProject.as_view(), name="add_project"),
    path("", Projects.as_view(), name="projects"),
    path("<slug:pk>", Projectdetail.as_view(), name="project_detail"),
    path("delete/<slug:pk>", DeleteProject.as_view(), name="delete_project"),
    path("edit/<slug:pk>", EditProject.as_view(), name="edit_project"),
    path("my_profile", MyProfile.as_view(), name="my_profile"),
    path("add_task/<slug:pk>", AddTask.as_view(), name="add_task"),
]
