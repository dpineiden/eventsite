from django.shortcuts import get_object_or_404, render
from .models import Pagina, Clasificacion
from django.conf import settings
# Create your views here.
import django
from django.conf import settings
from django.core.mail import send_mail


def home(request):
	pagina  = get_object_or_404(Pagina, slug_titulo="bienvenido-a-san-jose-home-care")
	static_media_url = settings.MEDIA_URL
	context = { 'pagina': pagina, 'static_media_url':static_media_url}
	return render(request, "index.html", context)


def ver_pagina(request, this_slug_titulo):
	pagina  = get_object_or_404(Pagina, slug_titulo=this_slug_titulo)
	static_media_url = settings.MEDIA_URL
	context = {'slug_titulo': this_slug_titulo, 'pagina': pagina, 'static_media_url':static_media_url}
	return render(request, 'pagina.html',context)

def ver_clasificacion(request, this_slug_tipo):
	clase  = get_object_or_404(Clasificacion, slug_tipo = this_slug_tipo)
	paginas  = Pagina.objects.filter( clasificacion = clase.id)
	context = {'slug_tipo':this_slug_tipo, 'clase': clase, 'paginas': paginas}
	return render(request, 'tipo.html',context)
