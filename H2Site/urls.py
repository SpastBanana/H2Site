from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('frontend.urls')),
    path('', include('frontend.urls')),
]

urlpatterns += staticfiles_urlpatterns()