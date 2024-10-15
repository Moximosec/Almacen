from django.shortcuts import render
from .models import Almacen

# Create your views here.
def pagina_inicio(request):
    context = {
        'show_sidebar': True  # Puedes cambiar esto basado en tu lógica de backend
    }
    return render(request, 'html/index.html')

def lista_almacen(request):
    productos = Almacen.objects.all()  # Obtener todos los registros
    return render(request, 'html/almacen.html', {'productos': productos})