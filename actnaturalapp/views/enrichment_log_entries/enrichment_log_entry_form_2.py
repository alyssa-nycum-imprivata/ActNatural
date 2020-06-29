from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from actnaturalapp.models import Animal, EnrichmentItem, AnimalEnrichmentItem, EnrichmentLogEntry


@login_required
def enrichment_log_entry_form_2(request):

    form_data = request.GET

    animal = form_data['animal']
    date = form_data['date']

    all_animal_enrichment_items = AnimalEnrichmentItem.objects.filter(animal_id=animal)
    enrichment_items = EnrichmentItem.objects.all()

    # grabs the approved animal enrichment items associated with a specific animal
    approved_animal_enrichment_items = []
    for item in all_animal_enrichment_items:
        if (item.is_manager_approved == True & item.is_vet_approved == True):
            approved_animal_enrichment_items.append(item)

    if request.method == 'GET':

        """GETS the approved animal enrichment items associated with a specific animal to populate in part 2 of the add new enrichment log entry form."""

        template = 'enrichment_log_entries/enrichment_log_entry_form_2.html'
        context = {
            "animal": animal,
            "date": date,
            "approved_animal_enrichment_items": approved_animal_enrichment_items,
            "enrichment_items": enrichment_items
        }

        return render(request, template, context)

@login_required
def enrichment_log_entry_edit_form_2(request, enrichment_log_entry_id):

    try:
        enrichment_log_entry = EnrichmentLogEntry.objects.get(pk=enrichment_log_entry_id)
    except: 
        return redirect(reverse('actnaturalapp:enrichment_log_entries'))

    form_data = request.GET

    animal = form_data['animal']
    date = form_data['date']

    all_animal_enrichment_items = AnimalEnrichmentItem.objects.filter(animal_id=animal)
    enrichment_items = EnrichmentItem.objects.all()

    # grabs the approved animal enrichment items associated with a specific animal
    approved_animal_enrichment_items = []
    for item in all_animal_enrichment_items:
        if (item.is_manager_approved == True & item.is_vet_approved == True):
            approved_animal_enrichment_items.append(item)

    if request.method == 'GET':

        """GETS the details of a specific enrichment log entry to pre-fill part 2 of the edit enrichment log entry form."""

        if request.user.employee.id == enrichment_log_entry.employee_id:

            template = 'enrichment_log_entries/enrichment_log_entry_form_2.html'
            context = {
                "animal": animal,
                "date": date,
                "approved_animal_enrichment_items": approved_animal_enrichment_items,
                "enrichment_items": enrichment_items,
                "enrichment_log_entry": enrichment_log_entry
            }

            return render(request, template, context)
        
        else: 
            return redirect(reverse('actnaturalapp:enrichment_log_entries'))





        