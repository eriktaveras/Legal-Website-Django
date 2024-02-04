from django.shortcuts import render, get_object_or_404
from .models import Blog
 
def allblogs(request):
    blogs = Blog.objects.all()  # Cambio aquí para obtener todos los blogs
    return render(request, 'blog/allblogs.html', {'blogs': blogs})
 
def detail(request, blog_id):
    blogdetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blogdetail})