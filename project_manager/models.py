from django.db import models
from django.contrib.auth.models import User

STATUS = (('To do', "To do"), ('In progress', "In progress"), ('Done', "Done"))

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, unique=True, null=False, blank=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="project_creation")
    description = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.title


class Task(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False)
    owned_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="task_owner")
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="task_creator")
    description = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20, choices=STATUS, default='To do',
        null=False, blank=False)
    deadline = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.title