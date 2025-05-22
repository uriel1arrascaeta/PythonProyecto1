# blog/views.py

from django.shortcuts import render, redirect
from .models import Autor, Categoria, Post
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaForm


def index(request):
    return render(request, "blog/index.html")


def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_posts')
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {'form': form})


def listar_posts(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {'posts': posts})


def buscar_post(request):
    resultados = []
    if request.method == 'GET':
        form = BusquedaForm(request.GET)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultados = Post.objects.filter(titulo__icontains=titulo)
    else:
        form = BusquedaForm()
    return render(request, "blog/search.html", {"form": form, "resultados": resultados})


def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('listar_posts')
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_form.html", {'form': form, 'editar': True})


def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('listar_posts')
    return render(request, "blog/confirmar_eliminar.html", {'post': post})
