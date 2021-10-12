from django.contrib import admin
from django.urls import path
from .views import viewdeltaStatusses, createdeltaStatus

urlpatterns = [
    path('view-delta-statusses/', viewdeltaStatusses.as_view()),
    path('create-delta-status/', createdeltaStatus.as_view()),
]
