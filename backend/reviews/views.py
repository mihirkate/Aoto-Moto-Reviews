from django.http import JsonResponse
from core.mongodb import vehicles_collection


def home(request):
    return JsonResponse({
        "message": "Auto Moto Reviews API"
    })