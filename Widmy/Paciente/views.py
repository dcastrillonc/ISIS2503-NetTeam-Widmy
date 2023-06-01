from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .logic.paciente_logic import get_pacientes
from django.contrib.auth.decorators import login_required
from .forms import PacienteForm
from Widmy_NetTeam.auth0backend import getRole

@login_required
def pacientes_list(request):
    role = getRole(request)
    if role == "Administrador":
        pacientes = get_pacientes()
        context = {
            'pacientes_list': pacientes
        }
        return render(request, 'Paciente/paciente.html', context)
    else:
        return HttpResponse("Acceso Denegado")

def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente create successful')
            return HttpResponseRedirect(reverse('pacienteCreate'))
        else:
            print(form.errors)
    else:
        form = PacienteForm()

    context = {
        'form': form,
    }

    return render(request, 'Paciente/pacienteCreate.html', context)
