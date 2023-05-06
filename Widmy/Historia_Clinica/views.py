from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .logic.historia_logic import get_historia, get_historias
from django.contrib.auth.decorators import login_required
from Widmy_NetTeam.auth0backend import getRole

@login_required
def historia_list(request):
    role = getRole(request)
    if role == "Administrador":
        historias = get_historias()
        context = {
            'historia_list': historias
        }
        return render(request, context)
    else:
        return HttpResponse("Acceso Denegado")

@login_required
def single_historia(request, id=0):
    historia = get_historia(id)
    context = {
        'historia': historia
    }
    return render(request, context)
