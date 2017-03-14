from django.contrib import admin
from .models import Pagina, Clasificacion
# Register your models here.



class PaginaAdmin(admin.ModelAdmin):
	list_display = ("clasificacion","titulo","fecha_publicacion")
	class Media:
		js = ('ckeditor/ckeditor/ckeditor.js')


admin.site.register(Pagina,PaginaAdmin)
admin.site.register(Clasificacion)