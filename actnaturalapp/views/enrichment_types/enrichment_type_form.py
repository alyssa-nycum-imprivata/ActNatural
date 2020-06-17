from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Team, EnrichmentType


@login_required
def enrichment_type_form(request):
    if request.method == 'GET':

        team = Team.objects.get(pk=request.user.employee.team_id)

        template = 'enrichment_types/enrichment_type_form.html'
        context = {
            "team": team
        }

        return render(request, template)

@login_required
def enrichment_type_edit_form(request, enrichment_type_id):

    if request.method == 'GET':
        
        enrichment_type = EnrichmentType.objects.get(pk=enrichment_type_id)
        team = Team.objects.get(pk=request.user.employee.team_id)

        template = 'enrichment_types/enrichment_type_form.html'
        context = {
            'enrichment_type': enrichment_type,
            'team': team
        }

        return render(request, template, context)