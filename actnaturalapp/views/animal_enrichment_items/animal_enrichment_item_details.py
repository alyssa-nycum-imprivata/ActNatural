from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import AnimalEnrichmentItem, Animal, EnrichmentItem


@login_required
def animal_enrichment_item_details(request, animal_enrichment_item_id):

    # grabs the specific animal enrichment item for the database
    animal_enrichment_item = AnimalEnrichmentItem.objects.get(pk=animal_enrichment_item_id)
    # grabs the animal attached to the animal enrichment item
    animal = Animal.objects.get(pk=animal_enrichment_item.animal_id)
    # grabs the enrichment item attached to the animal enrichment item
    enrichment_item = EnrichmentItem.objects.get(pk=animal_enrichment_item.enrichment_item_id)

    if request.method == 'POST':

        form_data = request.POST

        if (
            "actual_method" in form_data and form_data["actual_method"] == "DELETE"
        ):

            # the following both delete a specific animal enrichment item object

            if ("enrichment_page" in form_data):

                # If the user is on an enrichment item's details page (with a hidden input where name="enrichment_page"), this deletes the specified animal enrichment item and re-directs to the same enrichment item's details page 

                animal_enrichment_item.delete()

                return redirect(reverse('actnaturalapp:enrichment_item', args=[enrichment_item.id]))

            elif ("animal_page" in form_data):

                # If the user is on an animal's details page (with a hidden input where name="animal_page"), this deletes the specified animal enrichment item and re-directs to the same animal's details page 

                animal_enrichment_item.delete()

                return redirect(reverse('actnaturalapp:animal', args=[animal.id]))