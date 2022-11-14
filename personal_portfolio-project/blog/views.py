from django.shortcuts import render, get_object_or_404
from blog.models import Blog
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


def all_blogs(request: WSGIRequest) -> HttpResponse:
    """Возвращает из базы данных все объекты и передает в шаблон"""
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request: WSGIRequest, blog_id: int) -> HttpResponse:
    """Отображает конкретный блог"""
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
