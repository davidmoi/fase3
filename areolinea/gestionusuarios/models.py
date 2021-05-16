from django.db import models

# Create your models here.

class usuarioadmin(models.Model):
    usuario=models.CharField(max_length=30)
    contraseña=models.CharField(max_length=30)

class usuariooperador(models.Model):
    usuario=models.CharField(max_length=30)
    contraseña=models.CharField(max_length=30)

class registro(models.Model):
    clase=models.CharField(max_length=30)
    subtotal=models.CharField(max_length=30)
    total=models.CharField(max_length=30)
    descuento=models.CharField(max_length=30)
