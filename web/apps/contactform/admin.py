from django.contrib import admin
from django.db import models
from .models import Contact
# Register your models here.
from django.forms.widgets import CheckboxSelectMultiple

class ContactAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.ManyToManyField: {'widget': CheckboxSelectMultiple},
	}
	list_display = ("nombre","telefono","servicios","pub_date")




admin.site.register(Contact,ContactAdmin)