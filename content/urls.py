from django.urls import path
from . import views

urlpatterns = [
    path("projects", views.ProjectListView.as_view(), name="projects"),
    path("new_project/", views.project_new_view, name="project_new"),
]