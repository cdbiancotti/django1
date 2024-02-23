from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from producto.models import Auto
from django.urls import reverse_lazy


class Autos(ListView):
    model = Auto
    context_object_name = 'autos'
    template_name = "autos/autos.html"

    
class CrearAuto(CreateView):
    model = Auto
    template_name = "autos/crear_auto.html"
    fields = ['marca', 'modelo', 'fecha_fabricacion', 'descripcion']
    success_url = reverse_lazy('autos')
