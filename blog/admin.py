from django.contrib import admin

# Register your models here.
from .models import Post, Autor, Categoria


admin.site.register(Post)
admin.site.register(Autor)
admin.site.register(Categoria)
