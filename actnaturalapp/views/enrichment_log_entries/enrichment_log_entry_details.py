from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from actnaturalapp.models import EnrichmentLogEntry, Animal


@login_required 
def enrichment_log_entry_details(request, enrichment_log_entry_id):

    enrichment_log_entry = EnrichmentLogEntry.objects.get(pk=enrichment_log_entry_id)
    animal = Animal.objects.get(pk=enrichment_log_entry.animal_id)
    
    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
        ):

            enrichment_log_entry = EnrichmentLogEntry.objects.get(pk=enrichment_log_entry_id)

            if (form_data["actual_method"] == "DELETE"):

                if ("animal_page" in form_data):
                    
                    enrichment_log_entry.delete()

                    return redirect(reverse('actnaturalapp:animal', args=[animal.id]))

                else:

                    '''Deletes an enrichment log entry and re-directs to the main enrichment log page'''

                    enrichment_log_entry.delete()

                    return redirect(reverse('actnaturalapp:enrichment_log_entries'))

            elif (form_data["actual_method"] == "PUT"):

                '''Updates an enrichment log entry and re-directs to the main enrichment log page'''

                enrichment_log_entry.employee_id = request.user.employee.id
                enrichment_log_entry.animal_id = form_data['animal']
                enrichment_log_entry.enrichment_item_id = form_data['enrichment_item']
                enrichment_log_entry.date = form_data['date']
                enrichment_log_entry.note = form_data['note']

                enrichment_log_entry.save()

                return redirect(reverse('actnaturalapp:enrichment_log_entries'))