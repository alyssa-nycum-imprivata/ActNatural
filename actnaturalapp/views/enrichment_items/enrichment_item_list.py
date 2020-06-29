from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import EnrichmentItem, EnrichmentType, AnimalEnrichmentItem, Animal


@login_required
def enrichment_item_list(request, enrichment_type_id=None):

    if request.method == 'GET':

        """GETS all of the enrichment type and enrichment item objects associated with the logged in user's team."""
        
        enrichment_items = EnrichmentItem.objects.filter(team_id=request.user.employee.team_id)
        enrichment_types = EnrichmentType.objects.filter(team_id=request.user.employee.team_id)

        template = 'enrichment_items/enrichment_item_list.html'
        context = {
            'enrichment_items': enrichment_items,
            'enrichment_types': enrichment_types
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        form_files = request.FILES

        if (
            "note" in form_data
        ):

            """Makes a POST request to add a new enrichment item and then re-directs to that new enrichment item's details page."""

            new_enrichment_item = EnrichmentItem.objects.create(
                team_id = request.user.employee.team_id,
                name = form_data['name'],
                enrichment_type_id = form_data['enrichment_type'],
                note = form_data['note'],
                image = form_files['image']
            )

            """Gets the values from the selected checkboxes and makes a POST request for each animal enrichment item object that the user selected to get approved for a specific enrichment item, then re-directs to the new enrichment item's details page."""

            selected_animals = form_data.getlist('animals')

            for animal in selected_animals:
                animal_instance = Animal.objects.get(pk=animal)
                new_animal_enrichment_item = AnimalEnrichmentItem.objects.create(
                    animal = animal_instance,
                    enrichment_item = new_enrichment_item,
                    is_manager_approved = False,
                    is_vet_approved = False
                )

            return redirect(reverse('actnaturalapp:enrichment_item', args=[new_enrichment_item.id]))

        elif (
            "actual_method" in form_data
        ):

            enrichment_type = EnrichmentType.objects.get(pk=enrichment_type_id)

            if (form_data["actual_method"] == "DELETE"):

                """DELETES a specific enrichment type and then re-directs to the enrichment items list page."""

                enrichment_type.delete()

                return redirect(reverse('actnaturalapp:enrichment_items'))

            elif (form_data["actual_method"] == "PUT"):

                """Makes a PUT request to edit a specific enrichment type and then re-directs to the enrichment items list page."""

                enrichment_type.team_id = request.user.employee.team_id
                enrichment_type.name = form_data["name"]

                enrichment_type.save()

                return redirect(reverse('actnaturalapp:enrichment_items'))

        else:

            """Makes a POST request to add a new enrichment type and then re-directs to the add enrichment item form."""

            new_enrichment_type = EnrichmentType.objects.create(
                team_id = request.user.employee.team_id,
                name = form_data['name']
            )

            return redirect(reverse('actnaturalapp:enrichment_item_form'))