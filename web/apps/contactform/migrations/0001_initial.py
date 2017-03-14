# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('asunto', models.CharField(max_length=120)),
                ('mensaje', models.TextField()),
            ],
            options={
                'verbose_name': 'Formulario de Contacto',
                'verbose_name_plural': 'Formularios de Contacto',
                'ordering': ('pub_date', 'nombre'),
            },
        ),
    ]
