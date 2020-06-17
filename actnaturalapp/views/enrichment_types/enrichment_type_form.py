from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from actnaturalapp.models import Team, EnrichmentType


@login_required
def enrichment_type_form(request):
    if request.method == 'GET':

        # team = Team.objects.get(pk=request.user.employee.team_id)

        template = 'enrichment_types/enrichment_type_form.html'
        # context = {
        #     "team": team
        # }

        return render(request, template)