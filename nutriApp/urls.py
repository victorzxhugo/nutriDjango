from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('novo-paciente/', views.cadastrar_paciente, name='novo-paciente'),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('pacientes/editar/<int:paciente_id>/', views.editar_paciente, name='editar-paciente'),
    path('minhas-medidas/<int:paciente_id>/', views.minhas_medidas, name='minhas-medidas'),



]
