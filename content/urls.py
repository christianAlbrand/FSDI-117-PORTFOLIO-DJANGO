from django.urls import path
from . import views

urlpatterns = [
    path("project", views.projects_views, name="project")
]