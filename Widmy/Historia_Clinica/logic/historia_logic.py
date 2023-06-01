from ..models import Historia_Clinica

def get_historias():
    queryset = Historia_Clinica.objects.all()
    return (queryset)

def create_historia(form):
    historia = form.save()
    historia.save()
    return ()

def get_historia(id):
    historia = Historia_Clinica.objects.raw("SELECT * FROM historiasclinicas_historiaclinica WHERE id=%s" % id)[0]
    return (historia)