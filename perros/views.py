from django.shortcuts import render
from .models import PerroPerdido

def lista_perros(request):
    perros = PerroPerdido.objects.all().order_by('-fecha')
    return render(request, 'perros/lista_perros.html', {'perros': perros})
