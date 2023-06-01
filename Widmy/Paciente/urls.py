from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('Pacientes/', views.pacientes_list),
    path('PacienteCreate/', csrf_exempt(views.paciente_create), name='pacienteCreate'),
]