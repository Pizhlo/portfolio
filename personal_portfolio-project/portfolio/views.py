from django.shortcuts import render
from .models import Project
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


def home(request: WSGIRequest) -> HttpResponse:
    """Главная страница сайта"""
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'obj': projects})
