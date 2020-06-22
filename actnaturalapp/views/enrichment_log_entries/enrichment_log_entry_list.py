from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from actnaturalapp.models import EnrichmentLogEntry, Employee
import datetime


@login_required
def enrichment_log_entry_list(request):

    if request.method == 'GET':

        '''Gets all enrichment log entries for all employees on the logged in user's team and displays them on the main enrichment log page''' 

        employees = Employee.objects.filter(team_id=request.user.employee.team_id)
        users = User.objects.all()

        enrichment_log_entries = []
        for employee in employees:
            employee_entries = EnrichmentLogEntry.objects.filter(employee_id=employee.id)
            for entry in employee_entries:
                enrichment_log_entries.append(entry)

        dates = []
        for date in enrichment_log_entries:
            date = date.date
            dates.append(date)

        dates = set(dates)
        dates = list(dates)

        dates = sorted(dates, key=lambda date:date, reverse=True)

        template = 'enrichment_log_entries/enrichment_log_entry_list.html'
        context = {
            'enrichment_log_entries': enrichment_log_entries,
            'users': users,
            'dates': dates
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        '''Posts a new enrichment log entry and re-directs to the main enrichment log page'''
    
        new_enrichment_log_entry = EnrichmentLogEntry.objects.create(
            employee_id = request.user.employee.id,
            animal_id = form_data['animal'],
            enrichment_item_id = form_data['enrichment_item'],
            date = form_data['date'],
            note = form_data['note']
        )

        return redirect(reverse('actnaturalapp:enrichment_log_entries'))