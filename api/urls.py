from django.contrib import admin
from django.urls import path
from .views import viewVehicleStatusses, createVehicleStatus

urlpatterns = [
    path('view-vehicle-statusses/', viewVehicleStatusses.as_view()),
    path('create-vehicle-status/', createVehicleStatus.as_view()),
]
