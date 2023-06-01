from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('Consultas/', views.consultas_list),
    path('ConsultaCreate/', csrf_exempt(views.consulta_create), name='consultaCreate'),
]