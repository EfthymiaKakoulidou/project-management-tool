from django.contrib import admin
from .models import Project, Task, Profile


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "deadline")

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('project', "title", 'user', "deadline","status")

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "bio", "created_on")
