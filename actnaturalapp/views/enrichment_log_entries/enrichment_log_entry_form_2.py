from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from actnaturalapp.models import Animal, EnrichmentItem, AnimalEnrichmentItem, EnrichmentLogEntry


@login_required
def enrichment_log_entry_form_2(request):

    form_data = request.GET

    animal = form_data['animal']
    date = form_data['date']

    animal_enrichment_items = AnimalEnrichmentItem.objects.filter(animal_id=animal)
    enrichment_items = EnrichmentItem.objects.all()

    if request.method == 'GET':

        template = 'enrichment_log_entries/enrichment_log_entry_form_2.html'
        context = {
            "animal": animal,
            "date": date,
            "animal_enrichment_items": animal_enrichment_items,
            "enrichment_items": enrichment_items
        }

        return render(request, template, context)

@login_required
def enrichment_log_entry_edit_form_2(request, enrichment_log_entry_id):

    enrichment_log_entry = EnrichmentLogEntry.objects.get(pk=enrichment_log_entry_id)

    form_data = request.GET

    animal = form_data['animal']
    date = form_data['date']

    animal_enrichment_items = AnimalEnrichmentItem.objects.filter(animal_id=animal)
    enrichment_items = EnrichmentItem.objects.all()

    if request.method == 'GET':

        template = 'enrichment_log_entries/enrichment_log_entry_form_2.html'
        context = {
            "animal": animal,
            "date": date,
            "animal_enrichment_items": animal_enrichment_items,
            "enrichment_items": enrichment_items,
            "enrichment_log_entry": enrichment_log_entry
        }

        return render(request, template, context)




        