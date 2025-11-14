from django.urls import path
from . import views

app_name = 'torneos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('torneos/', views.catalogo, name='catalogo'),
    path('torneos/<int:pk>/', views.detalle_torneo, name='detalle_torneo'),
    path('preinscripcion/', views.preinscripcion, name='preinscripcion'),
]
