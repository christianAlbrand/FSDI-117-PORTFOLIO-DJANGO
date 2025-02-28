from django.shortcuts import render, redirect
from .models import Project
from django.views.generic import ListView
from .forms import ProjectForm

# # Create your views here.
# def projects_views(request):
#     projects = Project.objects.all()
#     return render(request, 'pages/project_list.html', {"projects": projects})

class ProjectListView(ListView):
    model = Project
    template_name = "pages/project_list.html"
    context_object_name = "projects"

def project_new_view(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("projects")
    else:
        form = ProjectForm()

    return render(request, "pages/project_new.html", {"form": form})

