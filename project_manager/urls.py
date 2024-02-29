from django.urls import path
from django.urls import reverse
from .views import (
    AddProject, Projects, Projectdetail, ProfileDetail,
    DeleteProject, EditProject, AddProfile, AddTask, Profiles
)

urlpatterns = [
    path("add_project", AddProject.as_view(), name="add_project"),
    path("", Projects.as_view(), name="projects"),
    path('project_detail/<slug:pk>/', Projectdetail.as_view(), name="project_detail"),
    path("delete/<slug:pk>", DeleteProject.as_view(), name="delete_project"),
    path("edit/<slug:pk>", EditProject.as_view(), name="edit_project"),
    path("add_profile/", AddProfile.as_view(), name="add_profile"),
    path("profile_detail/<slug:pk>/", ProfileDetail.as_view(), name="profile_detail"),
    path("add_task/<slug:pk>", AddTask.as_view(), name="add_task"),
    path("profiles/", Profiles.as_view(), name="profiles"),
]
    
