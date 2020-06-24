from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Employee, Team, AnimalEnrichmentItem

@login_required
def base(request):

    employee = Employee.objects.get(pk=request.user.employee.id)
    team = Team.objects.get(pk=request.user.employee.team_id)

    all_animal_enrichment_items = AnimalEnrichmentItem.objects.all()

    team_animal_enrichment_items = []
    for item in all_animal_enrichment_items:
        if item.animal.team_id == request.user.employee.team_id:
            team_animal_enrichment_items.append(item)

    unapproved_team_animal_enrichment_items = []
    for item in team_animal_enrichment_items:
        if item.is_manager_approved == False:
            unapproved_team_animal_enrichment_items.append(item)
    print("ITEMS", unapproved_team_animal_enrichment_items)
    
    count = 0
    for item in unapproved_team_animal_enrichment_items:
        count += 1
    print("COUNT", count)

    if request.method == 'GET':

        template = 'shared/base.html'
        context = {
            'employee': employee,
            'team': team,
            'count': count
        }

        return render(request, template, context)