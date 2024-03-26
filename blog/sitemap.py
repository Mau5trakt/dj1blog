from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        # Retorna un QuerySet de objetos para incluir en el sitemap
        # Por defecto Django llama a la funcion get_absolute_url()
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated
