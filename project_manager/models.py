from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = (("To do", "To do"), ("In progress", "In progress"), ("Done", "Done"))


class Project(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False, blank=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="project_creation"
    )
    description = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.title


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="task_creator"
    )
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="task_owner"
    )
    description = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20, choices=STATUS, default="To do", null=False, blank=False
    )
    deadline = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.title

class Profile(models.Model):
    first_name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    last_name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    featured_image = CloudinaryField('image', default='placeholder')
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="name"
    )
    job_title = models.CharField(max_length=200, unique=True, null=False, blank=False)
    bio = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name