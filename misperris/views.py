
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import registroMascota
from django.contrib import messages

from .forms import MascotaForm

def index(request):
    mascotas = registroMascota.objects.order_by('fecha_publicacion')
    return render(request, 'misperris/index.html', { 'mascotas': mascotas })

def mascota_view(request):
    
    if request.method == 'POST':
        form = MascotaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha registrado mascota exitosamente')
    else:
        form = MascotaForm()
    
    return render(request, 'misperris/mascota_form.html', {'form':form})

