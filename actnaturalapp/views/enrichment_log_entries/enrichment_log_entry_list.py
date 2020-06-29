from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from actnaturalapp.models import EnrichmentLogEntry, Employee
import datetime


@login_required
def enrichment_log_entry_list(request):

    if request.method == 'GET':

        """GETS all of the enrichment log entries from all of the employees on the logged in user's team"""

        employees = Employee.objects.filter(team_id=request.user.employee.team_id)
        users = User.objects.all()

        # grabs all of the enrichment log entries from the employees on the logged in user's team
        enrichment_log_entries = []
        for employee in employees:
            employee_entries = EnrichmentLogEntry.objects.filter(employee_id=employee.id)
            for entry in employee_entries:
                enrichment_log_entries.append(entry)

        # grabs the date on each enrichment log entry
        dates = []
        for date in enrichment_log_entries:
            date = date.date
            dates.append(date)

        # gets a unique list of those dates
        dates = set(dates)
        dates = list(dates)

        # sorts those dates from most recent to least recent
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

        """Makes a POST request to add a new enrichment log entry and then re-direct to the enrichment log entries list page."""
    
        new_enrichment_log_entry = EnrichmentLogEntry.objects.create(
            employee_id = request.user.employee.id,
            animal_id = form_data['animal'],
            enrichment_item_id = form_data['enrichment_item'],
            date = form_data['date'],
            note = form_data['note']
        )

        return redirect(reverse('actnaturalapp:enrichment_log_entries'))