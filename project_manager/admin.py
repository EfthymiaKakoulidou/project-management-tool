from django.contrib import admin
from .models import Project, Task, Note

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'deadline')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'owned_by', 'created_by', 'deadline')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'message', 'created_on')