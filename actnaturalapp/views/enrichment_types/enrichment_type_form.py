from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Team, EnrichmentType


@login_required
def enrichment_type_form(request):
    if request.method == 'GET':

        """GETS the logged in user's team object to save in the add new enrichment type form."""

        team = Team.objects.get(pk=request.user.employee.team_id)

        template = 'enrichment_types/enrichment_type_form.html'
        context = {
            "team": team
        }

        return render(request, template)

@login_required
def enrichment_type_edit_form(request, enrichment_type_id):

    try:
        enrichment_type = EnrichmentType.objects.get(pk=enrichment_type_id)
    except:
        return redirect(reverse('actnaturalapp:enrichment_items'))

    if request.method == 'GET':

        """GETS the details of a specific enrichment type to pre-fill the edit enrichment type form."""

        if request.user.employee.team_id == enrichment_type.team_id:
        
            team = Team.objects.get(pk=request.user.employee.team_id)

            template = 'enrichment_types/enrichment_type_form.html'
            context = {
                'enrichment_type': enrichment_type,
                'team': team
            }

            return render(request, template, context)

        else:
            return redirect(reverse('actnaturalapp:enrichment_items'))