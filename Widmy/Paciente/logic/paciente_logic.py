from ..models import Paciente

def get_pacientes():
    queryset = Paciente.objects.all()
    pacientes_list = list(queryset)
    return pacientes_list

def create_paciente(form):
    paciente = form.save()
    paciente.save()
    return ()