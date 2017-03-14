from django.conf.urls import patterns,url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^contacto/$', views.formulario_contacto, name= 'formulario_contacto'),
]