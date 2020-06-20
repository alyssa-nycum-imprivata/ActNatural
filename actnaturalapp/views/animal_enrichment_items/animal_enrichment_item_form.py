from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import EnrichmentItem, Animal, AnimalEnrichmentItem


@login_required
def animal_enrichment_item_form(request, enrichment_item_id):

    if request.method == 'GET':
        
        all_animals = Animal.objects.filter(team_id=request.user.employee.team_id)
        enrichment_item = EnrichmentItem.objects.get(pk=enrichment_item_id)
        animal_enrichment = AnimalEnrichmentItem.objects.filter(enrichment_item_id=enrichment_item.id)
        approved_animals = []

        for animal in animal_enrichment:
            approved_animals.append(animal.animal)

        set_difference = set(all_animals) - set(approved_animals)
        unapproved_animals = list(set_difference)

        template = 'animal_enrichment_items/animal_enrichment_item_form.html'
        context = {
            'enrichment_item': enrichment_item,
            'unapproved_animals': unapproved_animals

        }

        return render(request, template, context)

@login_required
def animal_enrichment_item_form_2(request, animal_id):

    if request.method == 'GET':
        
        all_enrichment_items = EnrichmentItem.objects.filter(team_id=request.user.employee.team_id)
        animal = Animal.objects.get(pk=animal_id)
        animal_enrichment = AnimalEnrichmentItem.objects.filter(animal_id=animal.id)
        approved_enrichment = []

        for item in animal_enrichment:
            approved_enrichment.append(item.enrichment_item)

        set_difference = set(all_enrichment_items) - set(approved_enrichment)
        unapproved_enrichment = list(set_difference)

        template = 'animal_enrichment_items/animal_enrichment_item_form_2.html'
        context = {
            'animal': animal,
            'unapproved_enrichment': unapproved_enrichment

        }

        return render(request, template, context)