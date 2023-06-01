from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('HistoriasClinicas/', views.historia_list),
    path('HistoriaClinicaCreate/', csrf_exempt(views.historia_create), name='historiaClinicaCreate'),
]
