from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name="Cars"),
    path('AZ/', views.AZhome, name="AzCars"),
    path('RU/', views.RUhome, name="RuCars")
    
]