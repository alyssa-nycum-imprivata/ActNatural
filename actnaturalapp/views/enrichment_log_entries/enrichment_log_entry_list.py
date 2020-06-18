from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from actnaturalapp.models import EnrichmentLogEntry, Employee


@login_required
def enrichment_log_entry_list(request):

    if request.method == 'GET':

        employees = Employee.objects.filter(team_id=request.user.employee.team_id)
        users = User.objects.all()

        enrichment_log_entries = []
        for employee in employees:
            employee_entries = EnrichmentLogEntry.objects.filter(employee_id=employee.id)
            for entry in employee_entries:
                enrichment_log_entries.append(entry)

        enrichment_log_entries = sorted(enrichment_log_entries, key=lambda enrichment_log_entry: enrichment_log_entry.date, reverse=True)

        template = 'enrichment_log_entries/enrichment_log_entry_list.html'
        context = {
            'enrichment_log_entries': enrichment_log_entries,
            'users': users
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