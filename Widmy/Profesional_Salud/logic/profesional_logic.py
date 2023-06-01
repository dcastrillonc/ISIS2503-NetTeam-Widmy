from ..models import Profesional_Salud

def get_profesionales():
    queryset = Profesional_Salud.objects.all()
    profesionales_list = list(queryset)
    return profesionales_list

def create_profesional(form):
    profesional = form.save()
    profesional.save()
    return ()