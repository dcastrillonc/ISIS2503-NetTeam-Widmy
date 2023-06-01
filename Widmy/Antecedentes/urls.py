from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('Antecedentes/', views.antecedentes_list),
    path('AntecedenteCreate/', csrf_exempt(views.antecedente_create), name='antecedenteCreate'),
]