from django.shortcuts import render
from django.http import HttpResponse 
from .models import Post

def home(request):
    context = {
        'title': 'Blog_board',
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return HttpResponse(render(request, 'blog/about.html'))