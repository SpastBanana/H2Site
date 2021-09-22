from django.http import request
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.fileView, name='Filemanager'),
    path('openfolder/<str:urlDir>/', views.openfolderView, name='Filemanager-folder'),
    path('openfolder/<str:urlDir>/download/<str:urlFile>', views.downloadFile, name='Download the sellected file'),
]