# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
from django.db import models
from django import forms

# Create your models here.


class registroMascota(models.Model):
    estado_list = (
        ('Rescatado', 'Rescatado'),
        ('Disponible', 'Disponible'),
        ('Adoptado', 'Adoptado')
    )
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField("Nombre", max_length=200)
    raza_predominante = models.TextField("Raza predominante")
    estado = models.CharField(max_length=20,choices=estado_list)
    descripcion = models.TextField("Descripcion")
    imagen = CloudinaryField('imagen')
    fecha_publicacion = models.DateTimeField("Fecha Publicacion", blank=True, null=True)
    
    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre



