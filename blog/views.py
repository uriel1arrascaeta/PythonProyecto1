from django.shortcuts import render

from django.http import HttpResponse
from .models import Post
# Create your views here.


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def crear_post(request):

    return HttpResponse("<h1>Página para crear un nuevo post</h1>")
