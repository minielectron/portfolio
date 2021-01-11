from django.shortcuts import render
from .models import Project

app_name="website"

def home(request):
    projects = Project.objects.all()
    return render(request,"website/home.html",{"projects": projects})