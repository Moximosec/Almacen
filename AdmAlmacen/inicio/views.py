from django.shortcuts import render

# Create your views here.
def pagina_inicio(request):
    context = {
        'show_sidebar': True  # Puedes cambiar esto basado en tu lógica de backend
    }
    return render(request, 'html/index.html')