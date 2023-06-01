from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .logic.profesional_logic import get_profesionales
from django.contrib.auth.decorators import login_required
from .forms import ProfesionalesForm
from Widmy_NetTeam.auth0backend import getRole

@login_required
def profesionales_list(request):
    role = getRole(request)
    if role == "Administrador":
        profesionales = get_profesionales()
        context = {
            'profesionales_list': profesionales
        }
        return render(request, 'ProfesionalesSalud/profesionales.html', context)
    else:
        return HttpResponse("Acceso Denegado")

def profesional_create(request):
    if request.method == 'POST':
        form = ProfesionalesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profesional de la Salud create successful')
            return HttpResponseRedirect(reverse('profesionalCreate'))
        else:
            print(form.errors)
    else:
        form = ProfesionalesForm()

    context = {
        'form': form,
    }

    return render(request, 'ProfesionalesSalud/profesionalCreate.html', context)