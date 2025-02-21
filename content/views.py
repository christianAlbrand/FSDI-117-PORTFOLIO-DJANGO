from django.shortcuts import render
from .models import Project

# Create your views here.
def projects_views(request):
    projects = Project.objects.all()
    return render(request, 'pages/project_list.html', {"projects": projects})