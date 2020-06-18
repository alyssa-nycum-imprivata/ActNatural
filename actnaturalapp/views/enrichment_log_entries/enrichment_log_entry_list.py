from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from actnaturalapp.models import EnrichmentLogEntry, Employee


@login_required
def enrichment_log_entry_list(request, enrichment_log_entry_id=None):

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

        if (
            "actual_method" in form_data
        ):

            enrichment_log_entry = EnrichmentLogEntry.objects.get(pk=enrichment_log_entry_id)

            if (form_data["actual_method"] == "DELETE"):

                enrichment_log_entry.delete()

                return redirect(reverse('actnaturalapp:enrichment_log_entries'))

            elif (form_data["actual_method"] == "PUT"):

                enrichment_log_entry.employee_id = request.user.employee.id
                enrichment_log_entry.animal_id = form_data['animal']
                enrichment_log_entry.enrichment_item_id = form_data['enrichment_item']
                enrichment_log_entry.date = form_data['date']
                enrichment_log_entry.note = form_data['note']

                enrichment_log_entry.save()

                return redirect(reverse('actnaturalapp:enrichment_log_entries'))

        else:
        
            new_enrichment_log_entry = EnrichmentLogEntry.objects.create(
                employee_id = request.user.employee.id,
                animal_id = form_data['animal'],
                enrichment_item_id = form_data['enrichment_item'],
                date = form_data['date'],
                note = form_data['note']
            )

            return redirect(reverse('actnaturalapp:enrichment_log_entries'))