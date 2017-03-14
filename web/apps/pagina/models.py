from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from . import managers
#ckeditor model
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
#slug
from autoslug import AutoSlugField
import itertools
from django.utils import timezone
from datetime import datetime,time
from django.contrib.sitemaps import ping_google
def get_upload_pagina_file_name(instance, filename):
    return "imagenes/paginas/%s/%s" %(instance.slug_titulo, filename)

class Pagina(models.Model):
    titulo = models.CharField(max_length=100)
    slug_titulo =  AutoSlugField(unique=True,blank=True,populate_from='titulo', editable=True)
    imagen = models.ImageField(upload_to=get_upload_pagina_file_name, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    resumen = models.TextField(default="Escribe un resumen")
    cuerpo = RichTextUploadingField()   
    clasificacion = models.ForeignKey('Clasificacion',blank=True,null=True)

    @models.permalink
    def get_absolute_url(self):
        return 'pagina:post', (self.slug_titulo,)

    @property
    def Pagina(self):
        return self.titulo

    class Meta:
        verbose_name = _("Página")
        verbose_name_plural = _("Páginas")
        ordering = ("clasificacion","fecha_publicacion")

    def __str__(self):
        return self.titulo

    def save(self):
        super(Pagina,self).save()
        try:
            ping_google()
        except Exception:
            pass

class Clasificacion(models.Model):
    tipo = models.CharField(max_length=20, unique=True)
    slug_tipo =   AutoSlugField(blank=True,populate_from='tipo', editable=True)
    descripccion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now=True)

    @models.permalink
    def get_absolute_url(self):
        return 'clasificacion:post', (self.slug_tipo,)

    @property
    def Clasificacion(self):
        return self.tipo

    class Meta:
        verbose_name = _("Clasificación")
        verbose_name_plural = _("Clasificaciones")
        ordering = ("tipo","fecha_publicacion")

    def __str__(self):
        return self.tipo