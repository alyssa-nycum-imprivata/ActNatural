from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from actnaturalapp.models import Animal, EnrichmentItem, AnimalEnrichmentItem


@login_required
def enrichment_log_entry_details(request, animal_id):

    animal = Animal.objects.get(pk=animal_id)
    animal_enrichment_items = AnimalEnrichmentItem.objects.filter(animal_id=animal.id)
    enrichment_items = EnrichmentItem.objects.all()

    if request.method == 'GET':

        template = 'enrichment_log_entries/enrichment_log_entry_form_2.html'
        context = {
            "animal": animal,
            "animal_enrichment_items": animal_enrichment_items,
            "enrichment_items": enrichment_items
        }

        return render(request, template, context)