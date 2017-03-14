from django.db import models
import geocoder
# Create your models here.
from django.utils import timezone
from datetime import datetime,time
from autoslug import AutoSlugField

def get_upload_pagina_file_name(instance, filename):
    return "imagenes/actividades/%s/%s" %(instance.slug_nombre, filename)

class Lugar(models.Model):
    nombre=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    comuna=models.CharField(max_length=100)

class Actividad(models.Model):
    nombre=models.CharField(max_length=100)
    slug_nombre =  AutoSlugField(unique=True,blank=True,populate_from='nombre', editable=True)
    fecha=models.DateTimeField(auto_now=False)
    imagen=models.ImageField(upload_to=get_upload_pagina_file_name, blank=True)
    lugar=models.ForeignKey('Lugar', blank=True, null=True)
    clasificacion = models.ForeignKey('Clasificacion',blank=True,null=True)

    @models.permalink
    def get_absolute_url(self):
        return 'pagina:post', (self.slug_nombre,)

class Clasificacion(models.Model):
    tipo = models.CharField(max_length=20, unique=True)
    slug_tipo =   AutoSlugField(blank=True,populate_from='tipo', editable=True)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now=True)

    @models.permalink
    def get_absolute_url(self):
        return 'clasificacion:post', (self.slug_tipo,)
