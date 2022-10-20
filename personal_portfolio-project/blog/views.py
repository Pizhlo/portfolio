from django.shortcuts import render
from blog.models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    print(blogs)
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})
