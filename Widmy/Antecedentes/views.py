from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import AntecedenteForm
from .logic.antecedentes_logic import get_antecedentes
from Widmy_NetTeam.auth0backend import getRole

@login_required
def antecedentes_list(request):
    role = getRole(request)
    if role == "Administrador":
        antecedentes = get_antecedentes()
        context = {
            'antecedentes_list': antecedentes
        }
        return render(request, 'Antecedentes/antecedentes.html', context)
    else:
        return HttpResponse("Acceso Denegado")

def antecedente_create(request):
    if request.method == 'POST':
        form = AntecedenteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Antecedente create successful')
            return HttpResponseRedirect(reverse('antecedenteCreate'))
        else:
            print(form.errors)
    else:
        form = AntecedenteForm()

    context = {
        'form': form,
    }

    return render(request, 'Antecedentes/antecedenteCreate.html', context)
