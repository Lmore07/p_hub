from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes
from pHub.classes import PHubService

class PHubController(APIView):
    parser_classes = [MultiPartParser]

    def __init__(self):
        self._pHubService = PHubService()

    @method_decorator(csrf_exempt)
    def post(self, request):
        files = request.FILES.getlist("files")

        response = self._pHubService.get_solutions_phub(files)

        return JsonResponse(response)
