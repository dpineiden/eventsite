from django.db import models
#soporte traslacion
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Contact(models.Model):
	nombre = models.CharField(max_length = 100)
	pub_date = models.DateTimeField(auto_now=True)
	telefono = models.IntegerField()
	email = models.EmailField()
	asunto = models.CharField(max_length = 120)
	mensaje = models.TextField()

	def __str__(self):
		return self.nombre

	@property
	def Contact(self):
		return self.nombre

	def servicios(self):
		return ", ".join([str(p) for p in self.servicio.all()])

	class Meta:
		verbose_name = _("Formulario de Contacto")
		verbose_name_plural = _("Formularios de Contacto")
		ordering = ("pub_date","nombre")
