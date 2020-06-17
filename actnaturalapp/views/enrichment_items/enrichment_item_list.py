from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import EnrichmentItem, EnrichmentType, AnimalEnrichmentItem, Animal


@login_required
def enrichment_item_list(request, enrichment_type_id=None):

    if request.method == 'GET':

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

            animals = Animal.objects.filter(team_id=request.user.employee.team_id)

            new_enrichment_item = EnrichmentItem.objects.create(
                team_id = request.user.employee.team_id,
                name = form_data['name'],
                enrichment_type_id = form_data['enrichment_type'],
                note = form_data['note'],
                is_manager_approved = False,
                is_vet_approved = False,
                image = form_files['image']
            )

            selected_animals = form_data.getlist('animals')

            for animal in selected_animals:
                animal_instance = Animal.objects.get(pk=animal)
                new_animal_enrichment_item = AnimalEnrichmentItem.objects.create(
                    animal = animal_instance,
                    enrichment_item = new_enrichment_item
                )

            return redirect(reverse('actnaturalapp:enrichment_item', args=[new_enrichment_item.id]))

        elif (
            "actual_method" in form_data
        ):

            enrichment_type = EnrichmentType.objects.get(pk=enrichment_type_id)

            if (form_data["actual_method"] == "DELETE"):

                enrichment_type.delete()

                return redirect(reverse('actnaturalapp:enrichment_items'))

            elif (form_data["actual_method"] == "PUT"):

                enrichment_type.team_id = request.user.employee.team_id
                enrichment_type.name = form_data["name"]

                enrichment_type.save()

                return redirect(reverse('actnaturalapp:enrichment_items'))

        else:

            new_enrichment_type = EnrichmentType.objects.create(
                team_id = request.user.employee.team_id,
                name = form_data['name']
            )

            return redirect(reverse('actnaturalapp:enrichment_item_form'))