from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import EnrichmentItem, Animal, AnimalEnrichmentItem


@login_required
def animal_enrichment_item_form(request, enrichment_item_id):

    if request.method == 'GET':

        """GETS the animals that have not yet been approved for a specific enrichment item."""
        
        all_animals = Animal.objects.filter(team_id=request.user.employee.team_id)
        enrichment_item = EnrichmentItem.objects.get(pk=enrichment_item_id)
        animal_enrichment = AnimalEnrichmentItem.objects.filter(enrichment_item_id=enrichment_item.id)
        
        # grabs the animals from the filtered animal enrichment item objects
        approved_animals = []
        for animal in animal_enrichment:
            approved_animals.append(animal.animal)

        # subtracts the unique approved animals from all animals to get the unapproved animals
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

        """GETS the enrichment items that have not yet been approved for a specific animal."""
        
        all_enrichment_items = EnrichmentItem.objects.filter(team_id=request.user.employee.team_id)
        animal = Animal.objects.get(pk=animal_id)
        animal_enrichment = AnimalEnrichmentItem.objects.filter(animal_id=animal.id)

        # grabs the enrichment items from the filtered animal enrichment item objects
        approved_enrichment = []
        for item in animal_enrichment:
            approved_enrichment.append(item.enrichment_item)

        # subtracts the unique approved enrichment items from all enrichment items to get the unapproved enrichment items
        set_difference = set(all_enrichment_items) - set(approved_enrichment)
        unapproved_enrichment = list(set_difference)

        template = 'animal_enrichment_items/animal_enrichment_item_form_2.html'
        context = {
            'animal': animal,
            'unapproved_enrichment': unapproved_enrichment

        }

        return render(request, template, context)