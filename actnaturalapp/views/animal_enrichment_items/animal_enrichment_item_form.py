from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import EnrichmentItem, Animal, AnimalEnrichmentItem


@login_required
def animal_enrichment_item_form(request, enrichment_item_id):

    if request.method == 'GET':
        
        # grabs all of the animals with a team_id that matches the logged in user's team_id
        all_animals = Animal.objects.filter(team_id=request.user.employee.team_id)
        # grabs the specific enrichment item the user wants to add animals to
        enrichment_item = EnrichmentItem.objects.get(pk=enrichment_item_id)
        # grabs all of the animal enrichment item objects associated with the specific enrichment item
        animal_enrichment = AnimalEnrichmentItem.objects.filter(enrichment_item_id=enrichment_item.id)
        
        # for every animal in the animal enrichment item objects, append the animal to the approved_animals list
        approved_animals = []
        for animal in animal_enrichment:
            approved_animals.append(animal.animal)

        # subtract each animal from the approved_animals list from the all_animals list and store the difference in the unapproved_animals list
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
        
        # grabs all of the enrichment items that has the same team_id as the logged in user's team_id
        all_enrichment_items = EnrichmentItem.objects.filter(team_id=request.user.employee.team_id)
        # grabs the specific animal the user wants to add enrichment items to
        animal = Animal.objects.get(pk=animal_id)
        # grabs all of the animal enrichment item objects associated with the specific animal
        animal_enrichment = AnimalEnrichmentItem.objects.filter(animal_id=animal.id)

        # for every enrichment item in the animal enrichment item objects, append the enrichment item to the approved_enrichment list
        approved_enrichment = []
        for item in animal_enrichment:
            approved_enrichment.append(item.enrichment_item)

        # subtract each enrichment item from the approved_enrichment list from the all_enrichment_items list and store the difference in the unapproved_enrichment list
        set_difference = set(all_enrichment_items) - set(approved_enrichment)
        unapproved_enrichment = list(set_difference)

        template = 'animal_enrichment_items/animal_enrichment_item_form_2.html'
        context = {
            'animal': animal,
            'unapproved_enrichment': unapproved_enrichment

        }

        return render(request, template, context)