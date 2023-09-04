from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .classes.service import PHubService
from django.shortcuts import render

@csrf_exempt
def phub_controller(request):
    if request.method == 'POST':
        files = request.FILES.getlist("archivo")
        p_hub_service = PHubService()
        response = p_hub_service.get_solutions_phub(files)
        
        coordinates = [{'x': node['coordinates']['x'], 'y': node['coordinates']['y']} for node in response['data']['solucionOptima']['servers'][0]['assignedClients']]
        coordenadas_soluciones_no_funcionadas = []
        
        for solucion in response['data']["solutiones"]:
            coordenadas_solucion_actual = []  # Lista para las coordenadas de la solución actual

            # Iterar a través de los servidores en esta solución
            for servidor in solucion["servers"]:
                # Iterar a través de los clientes asignados a este servidor
                for cliente in servidor["assignedClients"]:
                    coordenadas = cliente["coordinates"]
                    coordenadas_solucion_actual.append(coordenadas)

            # Agregar las coordenadas de esta solución a la lista general
            coordenadas_soluciones_no_funcionadas.append(coordenadas_solucion_actual)
    
        print(coordenadas_soluciones_no_funcionadas)
        return render(request, 'grafico.html', {'coordinates': coordinates, 'solucionesNoOptimas': coordenadas_soluciones_no_funcionadas})
        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
