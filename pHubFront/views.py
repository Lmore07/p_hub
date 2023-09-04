from django.http import JsonResponse
from django.shortcuts import render
from .forms import ArchivoForm
from pHub.views import phub_controller

def subir_archivo(request):
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            # Llama a la vista phub_controller
            return phub_controller(request)
        else:
            return JsonResponse({'error': 'Formulario inválido'}, status=400)
    else:
        form = ArchivoForm()
    return render(request, 'subir_archivo.html', {'form': form})
