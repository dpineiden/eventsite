from django.conf.urls import patterns,url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from .models import Pagina, Clasificacion
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PaginaSitemap, ClasificacionSitemap

sitemaps = {
    "paginas": PaginaSitemap(),
	'clasificacion': ClasificacionSitemap()
}

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^pagina/(?P<this_slug_titulo>[\w-]+)/$', views.ver_pagina, name= 'ver_pagina'),
	url(r'^clasificacion/(?P<this_slug_tipo>[\w-]+)/$', views.ver_clasificacion),
	url(r'^sitemap\.xml$',
		sitemap,
		{'sitemaps': sitemaps}),
]

