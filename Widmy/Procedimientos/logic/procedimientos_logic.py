from ..models import Procedimientos

def get_procedimientos():
    queryset = Procedimientos.objects.all()
    pacientes_list = list(queryset)
    return pacientes_list

def create_procedimiento(form):
    procedimiento = form.save()
    procedimiento.save()
    return ()