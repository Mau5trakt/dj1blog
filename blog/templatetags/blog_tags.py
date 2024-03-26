from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown


register = template.Library()

@register.simple_tag()
def total_posts(): #Nombre de la etiqueta #Django utiliza el nombre de la funcion como el nombre de la etiqueta
    return Post.published.count()

# Otra forma de darle un nombre a una etiqueta
@register.simple_tag(name="suma")
def sumita():
    return 2 + 2

#Para que las etiquetas esten disponibles en el proyecto hay que usar
# {%  load blog_tags %} al principio de la template (base.html)

# Creacion de una inclusion template tag
# Con una inclusion template tag se puede renderizar una plantilla con variables de contexto
# retornadas por my etiqueta de plantilla

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by("-publish")[:count]
    return {'latest_posts': latest_posts}


#Crear una template tag que retorne un Query Set

@register.simple_tag
def get_most_comented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))