from django.shortcuts import render
from .models import Car
from .serializer import CarSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

@extend_schema(
    request=CarSerializer,
    responses=CarSerializer,
)
class CarCreateView(APIView):
    def post(self, request):
        serializer = CarSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CarGetView(APIView):
    def get(self, request):
        cars = Car.objects.all()[:4]
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)