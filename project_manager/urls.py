from django.urls import path
from .views import AddProject


urlpatterns = [
    path('', AddProject.as_view(), name = 'add_project'),
]