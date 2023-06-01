from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('ProfesionalesSalud/', views.profesionales_list),
    path('ProfesionalSaludCreate/', csrf_exempt(views.profesional_create), name='profesionalCreate'),
]