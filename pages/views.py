from django.shortcuts import render

# Create your views here.
def my_first_view(request):
    return render(request, "base.html")

def about_view(request):
    return render(request, "pages/about_me.html")
