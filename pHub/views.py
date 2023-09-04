from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .classes.service import PHubService

@csrf_exempt
def phub_controller(request):
    if request.method == 'POST':
        files = request.FILES.getlist("archivo")
        p_hub_service = PHubService()
        response = p_hub_service.get_solutions_phub(files)
        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
