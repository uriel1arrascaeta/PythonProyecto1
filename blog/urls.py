# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('crear/', views.crear_post, name='crear_post'),
    path('posts/', views.listar_posts, name='listar_posts'),
    path('buscar/', views.buscar_post, name='buscar_post'),
    path('editar/<int:post_id>/', views.editar_post, name='editar_post'),
    path('eliminar/<int:post_id>/', views.eliminar_post, name='eliminar_post'),
]
