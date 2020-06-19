from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import EnrichmentItem, EnrichmentType, Employee, Team, AnimalEnrichmentItem, Animal



@login_required
def enrichment_item_details(request, enrichment_item_id):

    enrichment_item = EnrichmentItem.objects.get(pk=enrichment_item_id)
    enrichment_type = EnrichmentType.objects.get(pk=enrichment_item.enrichment_type_id)
    animal_enrichment_items = AnimalEnrichmentItem.objects.filter(enrichment_item_id=enrichment_item.id)
    employee = Employee.objects.get(pk=request.user.employee.id)
    team = Team.objects.get(pk=enrichment_item.team_id)

    if request.method == 'GET':

        if request.user.employee.team_id == enrichment_item.team_id:

            template = 'enrichment_items/enrichment_item_details.html'
            context = {
                "enrichment_item": enrichment_item,
                "enrichment_type": enrichment_type,
                "employee": employee,
                "team": team,
                "animal_enrichment_items": animal_enrichment_items
            }

            return render(request, template, context)

        else:
            return redirect(reverse('actnaturalapp:enrichment_items'))

    elif request.method == 'POST':

        form_data = request.POST
        form_files = request.FILES

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            if (
                "updated_photo" in form_data
            ):

                enrichment_item.team_id = request.user.employee.team_id
                enrichment_item.enrichment_type_id = enrichment_item.enrichment_type_id
                enrichment_item.name = enrichment_item.name
                enrichment_item.note = enrichment_item.note
                enrichment_item.is_manager_approved = enrichment_item.is_manager_approved
                enrichment_item.is_vet_approved = enrichment_item.is_vet_approved
                enrichment_item.image = form_files['image']

                enrichment_item.save()

                return redirect(reverse('actnaturalapp:enrichment_item', args=[enrichment_item.id]))

            else:
                enrichment_item.team_id = request.user.employee.team_id
                enrichment_item.enrichment_type_id = form_data['enrichment_type']
                enrichment_item.name = form_data['name']
                enrichment_item.note = form_data['note']
                enrichment_item.is_manager_approved = False
                enrichment_item.is_vet_approved = False
                enrichment_item.image = enrichment_item.image

                enrichment_item.save()

                return redirect(reverse('actnaturalapp:enrichment_item', args=[enrichment_item.id]))
    
        elif (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            
            enrichment_item.delete()

            return redirect(reverse('actnaturalapp:enrichment_items'))

        else:

            selected_animals = form_data.getlist('animals')

            for animal in selected_animals:
                animal_instance = Animal.objects.get(pk=animal)
                new_animal_enrichment_item = AnimalEnrichmentItem.objects.create(
                    animal = animal_instance,
                    enrichment_item = enrichment_item
                )

            return redirect(reverse('actnaturalapp:enrichment_item', args=[enrichment_item.id]))


    