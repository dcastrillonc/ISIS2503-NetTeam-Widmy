from ..models import ExamenMedico

def get_examenes():
    queryset = ExamenMedico.objects.all()
    return (queryset)

def create_examen(form):
    examen = form.save()
    examen.save()
    return ()