from django.urls import path
from producto import views

urlpatterns = [
    path('autos/', views.Autos.as_view(), name='autos'),
    path('autos/nuevo/', views.CrearAuto.as_view(), name='crear_auto')
]
