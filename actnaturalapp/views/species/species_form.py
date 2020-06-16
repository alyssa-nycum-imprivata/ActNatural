from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Species, Team, Employee


@login_required
def species_form(request):
    if request.method == 'GET':

        team = Team.objects.get(pk=request.user.employee.team_id)

        template = 'species/species_form.html'
        context = {
            "team": team
        }

        return render(request, template, context)

@login_required
def species_edit_form(request, species_id):

    if request.method == 'GET':
        
        species = Species.objects.get(pk=species_id)
        # employee = Employee.objects.get(pk=request.user.employee.id)
        team = Team.objects.get(pk=request.user.employee.team_id)

        template = 'species/species_form.html'
        context = {
            'species': species,
            'team': team
        }

        return render(request, template, context)