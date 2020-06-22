from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal, Employee, EnrichmentLogEntry
import datetime


@login_required
def enrichment_log_entry_form(request):
    if request.method == 'GET':
        
        employee = Employee.objects.get(pk=request.user.employee.id)
        animals = Animal.objects.filter(team_id=request.user.employee.team_id)

        date = str(datetime.date.today())

        template = 'enrichment_log_entries/enrichment_log_entry_form.html'
        context = {
            'employee': employee,
            'animals': animals,
            'date': date
        }

        return render(request, template, context)

@login_required
def enrichment_log_entry_edit_form(request, enrichment_log_entry_id):

    try:
        enrichment_log_entry = EnrichmentLogEntry.objects.get(pk=enrichment_log_entry_id)
    except:
        return redirect(reverse('actnaturalapp:enrichment_log_entries'))

    if request.method == 'GET':

        if request.user.employee.id == enrichment_log_entry.employee_id:
        
            employee = Employee.objects.get(pk=request.user.employee.id)
            animals = Animal.objects.filter(team_id=request.user.employee.team_id)

            enrichment_log_entry.date = str(enrichment_log_entry.date)

            template = 'enrichment_log_entries/enrichment_log_entry_form.html'
            context = {
                'employee': employee,
                'animals': animals,
                'enrichment_log_entry': enrichment_log_entry
            }

            return render(request, template, context)

        else:
            return redirect(reverse('actnaturalapp:enrichment_log_entries'))
            