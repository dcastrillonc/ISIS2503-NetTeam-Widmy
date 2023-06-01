from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('Procedimientos/', views.procedimientos_list),
    path('ProcedimientoCreate/', csrf_exempt(views.procedimiento_create), name='procedimientoCreate'),
]