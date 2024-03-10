from django.urls import path
from django.urls import reverse
from .views import (
    AddProject, Projects, Projectdetail, ProfileDetail,
    DeleteProject, EditProject, AddProfile, AddTask, Profiles,
    EditProfile, DeleteProfile, EditTask, DeleteTask, Tasks, Home, EditTaskStatus
)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('projects', Projects.as_view(), name="projects"),
    path('project_detail/<slug:pk>/', Projectdetail.as_view(), name="project_detail"),
    path("add_project", AddProject.as_view(), name="add_project"),
    path("delete/<slug:pk>", DeleteProject.as_view(), name="delete_project"),
    path("edit/<slug:pk>", EditProject.as_view(), name="edit_project"),
    path("add_profile/", AddProfile.as_view(), name="add_profile"),
    path("profile_detail/<slug:pk>/", ProfileDetail.as_view(), name="profile_detail"),
    path("add_task/<int:project_id>/", AddTask.as_view(), name="add_task"),
    path("profiles/", Profiles.as_view(), name="profiles"),
    path("delete_profile/<slug:pk>", DeleteProfile.as_view(), name="delete_profile"),
    path("edit_profile/<slug:pk>", EditProfile.as_view(), name="edit_profile"),
    path("delete_task/<slug:pk>", DeleteTask.as_view(), name="delete_task"),
    path("edit_task/<slug:pk>", EditTask.as_view(), name="edit_task"),
    path("my_tasks", Tasks.as_view(), name="my_tasks"),
    path("task/<slug:pk>", EditTaskStatus.as_view(), name="edit_task_status"),
]
    
