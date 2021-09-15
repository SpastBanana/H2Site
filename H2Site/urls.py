from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from frontend import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
]

urlpatterns += staticfiles_urlpatterns()