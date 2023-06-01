from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ExamenMedicoForm
from .logic.examenMedico_logic import get_examenes
from Widmy_NetTeam.auth0backend import getRole

@login_required
def examenes_list(request):
    role = getRole(request)
    if role == "Administrador":
        examenes = get_examenes()
        context = {
            'examenes_list': examenes
        }
        return render(request, 'ExamenMedico/examen.html', context)
    else:
        return HttpResponse("Acceso Denegado")

def examen_create(request):
    if request.method == 'POST':
        form = ExamenMedicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Examen Medico create successful')
            return HttpResponseRedirect(reverse('examenCreate'))
        else:
            print(form.errors)
    else:
        form = ExamenMedicoForm()

    context = {
        'form': form,
    }

    return render(request, 'ExamenMedico/examenCreate.html', context)