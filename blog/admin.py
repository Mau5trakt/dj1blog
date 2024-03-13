from django.contrib import admin
from .models import Post


# Register your models here.

#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status'] # Resumen centrado de los posts
    list_filter = ['status', 'created', 'publish', 'author'] #  Barra de filtros de la derecha
    search_fields = ['title', 'body'] # Barra de busqueda y campos por los que busca
    prepopulated_fields = {'slug': ('title',)} #Hacer que el slug se cree conforme se crea el titulo
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

