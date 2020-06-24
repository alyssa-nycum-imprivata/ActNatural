from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import AnimalEnrichmentItem, Animal, EnrichmentItem, Team, Species, EnrichmentType

@login_required
def animal_enrichment_items_pending_manager_approval(request):

    all_animal_enrichment_items = AnimalEnrichmentItem.objects.all()
    animals = Animal.objects.all()
    species = Species.objects.all()
    enrichment_types = EnrichmentType.objects.all()
    team = Team.objects.get(pk=request.user.employee.team_id)

    team_animal_enrichment_items = []
    for item in all_animal_enrichment_items:
        if item.animal.team_id == request.user.employee.team_id:
            team_animal_enrichment_items.append(item)

    unapproved_team_animal_enrichment_items = []
    for item in team_animal_enrichment_items:
        if item.is_manager_approved == False:
            unapproved_team_animal_enrichment_items.append(item)

    enrichment_items = []
    for item in unapproved_team_animal_enrichment_items:
        item = EnrichmentItem.objects.get(pk=item.enrichment_item.id)
        enrichment_items.append(item)

    enrichment_items = set(enrichment_items)
    enrichment_items = list(enrichment_items)

    if request.method == 'GET':

        if request.user.employee.position == "Manager":

            template = 'animal_enrichment_items/pending_manager_approval.html'
            context = {
                'animals': animals,
                'species': species,
                'enrichment_items': enrichment_items,
                'enrichment_types': enrichment_types,
                'team': team,
                'unapproved_team_animal_enrichment_items': unapproved_team_animal_enrichment_items
            }

            return render(request, template, context)

        else:
            return redirect(reverse('actnaturalapp:enrichment_items'))

    if request.method == 'POST':

        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            selected_items = form_data.getlist('items')

            for item in selected_items:
                animal_enrichment_item = AnimalEnrichmentItem.objects.get(pk=item)
                animal_enrichment_item.animal_id = animal_enrichment_item.animal_id
                animal_enrichment_item.enrichment_item_id = animal_enrichment_item.enrichment_item_id
                animal_enrichment_item.is_manager_approved = True
                animal_enrichment_item.is_vet_approved = animal_enrichment_item.is_vet_approved
                animal_enrichment_item.save()

            return redirect(reverse('actnaturalapp:animal_enrichment_items_pending_manager_approval'))



def animal_enrichment_items_pending_vet_approval(request):

    all_animal_enrichment_items = AnimalEnrichmentItem.objects.all()
    animals = Animal.objects.all()
    species = Species.objects.all()
    enrichment_items = EnrichmentItem.objects.all()
    enrichment_types = EnrichmentType.objects.all()

    unapproved_animal_enrichment_items = []
    for item in all_animal_enrichment_items:
        if item.is_vet_approved == False:
            unapproved_animal_enrichment_items.append(item)

    teams = []
    for item in unapproved_animal_enrichment_items:
        team = item.animal.team.name
        teams.append(team)

    teams = set(teams)
    teams = list(teams)

    if request.method == 'GET':

        if request.user.employee.position == "Vet":

            template = 'animal_enrichment_items/pending_vet_approval.html'
            context = {
                'animals': animals,
                'species': species,
                'enrichment_items': enrichment_items,
                'enrichment_types': enrichment_types,
                'teams': teams,
                'unapproved_animal_enrichment_items': unapproved_animal_enrichment_items
            }

            return render(request, template, context)

        else:
            return redirect(reverse('actnaturalapp:enrichment_items'))

    if request.method == 'POST':

        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            selected_items = form_data.getlist('items')

            for item in selected_items:
                animal_enrichment_item = AnimalEnrichmentItem.objects.get(pk=item)
                animal_enrichment_item.animal_id = animal_enrichment_item.animal_id
                animal_enrichment_item.enrichment_item_id = animal_enrichment_item.enrichment_item_id
                animal_enrichment_item.is_manager_approved = animal_enrichment_item.is_manager_approved
                animal_enrichment_item.is_vet_approved = True
                animal_enrichment_item.save()

            return redirect(reverse('actnaturalapp:animal_enrichment_items_pending_vet_approval'))