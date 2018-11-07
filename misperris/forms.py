from django import forms
from .models import registroMascota

class MascotaForm(forms.ModelForm):

    class Meta:
        model = registroMascota

        fields =  [
            'autor', 
            'nombre',
            'raza_predominante',
            'estado', 
            'descripcion',
            'imagen'

        ]
        labels = {
            'autor':'Responsable', 
            'nombre':'Nombre mascota',
            'raza_predominante' : 'Raza predominante',
            'estado' : 'Estado en que se encuentra', 
            'descripcion' : 'Descripcion ',
            'imagen' : 'Imagen'
        }
        widgets = {
            'autor' : forms.Select(attrs={'class':'form-control'}), 
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'raza_predominante' : forms.TextInput(attrs={'class':'form-control'}),
            'estado' : forms.Select(attrs={'class':'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class':'form-control'})
        }

    