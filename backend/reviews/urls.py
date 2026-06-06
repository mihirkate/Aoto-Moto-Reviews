from django.urls import path
from .views import CarCreateView, CarGetView

urlpatterns = [
    # path('', views.home),
    path('cars/post/', CarCreateView.as_view(), name='create-car'),
    path('cars/get4/', CarGetView.as_view(), name='get-car'),
]