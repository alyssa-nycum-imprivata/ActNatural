from django.shortcuts import render, redirect, reverse
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

    try:
        species = Species.objects.get(pk=species_id)
    except:
        return redirect(reverse('actnaturalapp:animals'))

    if request.method == 'GET':

        if request.user.employee.team_id == species.team_id:
        
            team = Team.objects.get(pk=request.user.employee.team_id)

            template = 'species/species_form.html'
            context = {
                'species': species,
                'team': team
            }

            return render(request, template, context)

        else:
            return redirect(reverse('actnaturalapp:animals'))
