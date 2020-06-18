from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import EnrichmentLogEntry


@login_required
def enrichment_log_entry_list(request):

    if request.method == 'GET':

        enrichment_log_entries = EnrichmentLogEntry.objects.all()

        template = 'enrichment_log_entries/enrichment_log_entry_list.html'
        context = {
            'enrichment_log_entries': enrichment_log_entries
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_enrichment_log_entry = EnrichmentLogEntry.objects.create(
            employee_id = request.user.employee.id,
            animal_id = form_data['animal'],
            enrichment_item_id = form_data['enrichment_item'],
            date = form_data['date'],
            note = form_data['note']
        )

        return redirect(reverse('actnaturalapp:enrichment_log_entries'))