from ..models import Antecedentes

def get_antecedentes():
    queryset = Antecedentes.objects.all()
    return (queryset)

def create_antecedente(form):
    antecedente = form.save()
    antecedente.save()
    return ()