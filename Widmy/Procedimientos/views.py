from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .logic.procedimientos_logic import get_procedimientos
from django.contrib.auth.decorators import login_required
from .forms import ProcedimientosForm
from Widmy_NetTeam.auth0backend import getRole

@login_required
def procedimientos_list(request):
    role = getRole(request)
    if role == "Administrador":
        procedimientos = get_procedimientos()
        context = {
            'procedimientos_list': procedimientos
        }
        return render(request, 'Procedimientos/procedimiento.html', context)
    else:
        return HttpResponse("Acceso Denegado")

def procedimiento_create(request):
    if request.method == 'POST':
        form = ProcedimientosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Procedimiento create successful')
            return HttpResponseRedirect(reverse('procedimientoCreate'))
        else:
            print(form.errors)
    else:
        form = ProcedimientosForm()

    context = {
        'form': form,
    }

    return render(request, 'Procedimientos/procedimientoCreate.html', context)