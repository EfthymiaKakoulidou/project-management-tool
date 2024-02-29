from django.urls import path
from django.urls import reverse
from .views import (
    AddProject, Projects, Projectdetail, ProfileDetail, TaskDetail,
    DeleteProject, EditProject, AddProfile, AddTask, Profiles,
    EditProfile, DeleteProfile, EditTask, DeleteTask
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
    path("delete/<slug:pk>", DeleteProfile.as_view(), name="delete_profile"),
    path("edit/<slug:pk>", EditProfile.as_view(), name="edit_profile"),
    path('task_detail/<slug:pk>/', TaskDetail.as_view(), name="task_detail"),
    path("delete/<slug:pk>", DeleteTask.as_view(), name="delete_task"),
    path("edit/<slug:pk>", EditTask.as_view(), name="edit_task"),
]
    
