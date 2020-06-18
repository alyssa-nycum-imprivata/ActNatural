from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal, EnrichmentItem, Employee, EnrichmentLogEntry


@login_required
def enrichment_log_entry_form(request):
    if request.method == 'GET':
        
        employee = Employee.objects.get(pk=request.user.employee.id)
        animals = Animal.objects.filter(team_id=request.user.employee.team_id)
        enrichment_items = EnrichmentItem.objects.filter(team_id=request.user.employee.team_id)


        template = 'enrichment_log_entries/enrichment_log_entry_form.html'
        context = {
            'employee': employee,
            'animals': animals,
            'enrichment_items': enrichment_items
        }

        return render(request, template, context)

@login_required
def enrichment_log_entry_edit_form(request, enrichment_log_entry_id):

    if request.method == 'GET':
        
        employee = Employee.objects.get(pk=request.user.employee.id)
        enrichment_log_entry = EnrichmentLogEntry.objects.get(pk=enrichment_log_entry_id)
        animals = Animal.objects.filter(team_id=request.user.employee.team_id)
        enrichment_items = EnrichmentItem.objects.filter(team_id=request.user.employee.team_id)

        enrichment_log_entry.date = str(enrichment_log_entry.date)

        template = 'enrichment_log_entries/enrichment_log_entry_form.html'
        context = {
            'employee': employee,
            'animals': animals,
            'enrichment_items': enrichment_items,
            'enrichment_log_entry': enrichment_log_entry
        }

        return render(request, template, context)