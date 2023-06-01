from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .logic.consulta_logic import get_consultas
from django.contrib.auth.decorators import login_required
from .forms import ConsultaForm
from Widmy_NetTeam.auth0backend import getRole

@login_required
def consultas_list(request):
    role = getRole(request)
    if role == "Administrador":
        consultas = get_consultas()
        context = {
            'consultas_list': consultas
        }
        return render(request, 'Consulta/consulta.html', context)
    else:
        return HttpResponse("Acceso Denegado")

def consulta_create(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Consulta create successful')
            return HttpResponseRedirect(reverse('consultaCreate'))
        else:
            print(form.errors)
    else:
        form = ConsultaForm()

    context = {
        'form': form,
    }

    return render(request, 'Consulta/consultaCreate.html', context)

