from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import AnimalEnrichmentItem, Animal, EnrichmentItem


@login_required
def animal_enrichment_item_details(request, animal_enrichment_item_id):

    animal_enrichment_item = AnimalEnrichmentItem.objects.get(pk=animal_enrichment_item_id)
    animal = Animal.objects.get(pk=animal_enrichment_item.animal_id)
    enrichment_item = EnrichmentItem.objects.get(pk=animal_enrichment_item.enrichment_item_id)

    if request.method == 'POST':

        form_data = request.POST

        if (
            "actual_method" in form_data and form_data["actual_method"] == "DELETE"
        ):

            animal_enrichment_item.delete()

            return redirect(reverse('actnaturalapp:enrichment_item', args=[enrichment_item.id]))

        # elif (
        #     "actual_method" in form_data and form_data["actual_method"] == "PUT"
        # ):

        #     note.employee_id = request.user.employee.id
        #     note.animal_id = animal.id
        #     note.date = form_data["date"]
        #     note.note = form_data["note"]

        #     note.save()

        #     return redirect(reverse('actnaturalapp:animal', args=[animal.id]))