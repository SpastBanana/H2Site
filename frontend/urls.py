from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.indexView, name='Home'),
    path('login', views.loginView, name="Login"),
    path('logout', views.logoutView, name="Logout"),
    path('register', views.registerView, name="Register"),
    path('profiel', views.profielView, name='Profiel'),
    path('dashboard', views.dashboardView, name='Dashboard'),
    path('downloads', views.downloadsView, name='Downloads'),
    path('data-analytics', views.dataAnalyticsView, name='Data-Analytics'),
    path('testcharts', views.testChartView, name='Test Charts'),
    path('logboek', views.logboekView, name='Logboek'),
    path('ass', views.liveData, name='kont')
]