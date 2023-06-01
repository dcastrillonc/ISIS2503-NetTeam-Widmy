from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('ExamenMedico/', views.examenes_list),
    path('ExamenCreate/', csrf_exempt(views.examen_create), name='examenCreate'),
]