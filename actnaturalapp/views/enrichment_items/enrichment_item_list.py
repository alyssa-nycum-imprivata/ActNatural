from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import EnrichmentItem, EnrichmentType, AnimalEnrichmentItem, Animal


@login_required
def enrichment_item_list(request, enrichment_type_id=None):

    if request.method == 'GET':
        
        # grabs the enrichment items with a team_id that matches the logged in user's team_id
        enrichment_items = EnrichmentItem.objects.filter(team_id=request.user.employee.team_id)
        # grabs the enrichment types with a team_id that matches the logged in user's team_id
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

            # if note is a property in form_data, post a new enrichment object

            new_enrichment_item = EnrichmentItem.objects.create(
                team_id = request.user.employee.team_id,
                name = form_data['name'],
                enrichment_type_id = form_data['enrichment_type'],
                note = form_data['note'],
                image = form_files['image']
            )

            # then also grab the checkbox value's where name="animals" and store them in the selected_animals array

            selected_animals = form_data.getlist('animals')

            # then for each animal in selected_animals, create an animal instance and then post a new animal enrichment item object with the animal instance as the animal and the above created enrichment item as the enrichment item and then re-direct to the new enrichment item's details page

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

                # if there's a hidden input with a value of "DELETE", then delete the specified enrichment type and re-direct to the enrichment_items list

                enrichment_type.delete()

                return redirect(reverse('actnaturalapp:enrichment_items'))

            elif (form_data["actual_method"] == "PUT"):

                # if there's a hidden input with a value of "PUT", then grab the edited form data and save the edited enrichment type object and re-direct to the enrichment items list

                enrichment_type.team_id = request.user.employee.team_id
                enrichment_type.name = form_data["name"]

                enrichment_type.save()

                return redirect(reverse('actnaturalapp:enrichment_items'))

        else:

            #  otherwise post a new enrichment type object with the data typed into the form and re-direct to the enrichment item form

            new_enrichment_type = EnrichmentType.objects.create(
                team_id = request.user.employee.team_id,
                name = form_data['name']
            )

            return redirect(reverse('actnaturalapp:enrichment_item_form'))