from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Participante(models.Model):
    CATEGORIA_CHOICES = (
        ('ORG', 'Organizadora'),
        ('EXP','Expositora'),
        ('PRT','Participante')
    )
    nombre = models.CharField(max_length=200, unique=True)
    fono = PhoneNumberField()
    email = models.EmailField()
    categoria=models.CharField(max_length=3, choices=CATEGORIA_CHOICES,default='PRT')


    class Meta:
        verbose_name=('Participante')
        verbose_name_plural=('Participantes')
        ordering=('nombre','categoria')

    def __str__(self):
        return "%s, f: %s" %(self.nombre,self.fono)
