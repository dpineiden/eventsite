from django.test import TestCase
from django.contrib.auth import get_user_model
from . import models
# Create your tests here.

class TestPaginaModel(TestCase):
	def test_pagina_creation(self):
		pagina = new Pagina()
		self.assertIsInstance(pagina.titulo) 

class TestClasificacionModel(TestCase):