from django.shortcuts import render
from .models import Project


def home(request):
    """Главная страница сайта"""
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'obj': projects})
