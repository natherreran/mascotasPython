# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misperris', '0005_registrousuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='registromascota',
            name='fecha_publicacion',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha Publicacion'),
        ),
    ]
