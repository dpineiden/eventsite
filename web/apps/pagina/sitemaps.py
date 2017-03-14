from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from .models import Pagina, Clasificacion

class PaginaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Pagina.objects.all()

    def lastmod(self, obj):
        return obj.fecha_publicacion

    def location(self, obj):
        return "/pagina/"+obj.slug_titulo

class ClasificacionSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Clasificacion.objects.all()

    def lastmod(self, obj):
        return obj.fecha_publicacion

    def location(self, obj):
        return "/clasificacion/"+obj.slug_tipo
