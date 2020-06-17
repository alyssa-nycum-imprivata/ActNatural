from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Employee, EnrichmentType, EnrichmentItem


@login_required
def enrichment_item_form(request):

    if request.method == 'GET':
        
        employee = Employee.objects.get(pk=request.user.employee.id)
        enrichment_types = EnrichmentType.objects.filter(team_id=request.user.employee.team_id)

        template = 'enrichment_items/enrichment_item_form.html'
        context = {
            'enrichment_types': enrichment_types,
            'employee': employee
        }

        return render(request, template, context)

@login_required
def enrichment_item_edit_form(request, enrichment_item_id):
    
    if request.method == 'GET':

        enrichment_item = EnrichmentItem.objects.get(pk=enrichment_item_id)
        enrichment_types = EnrichmentType.objects.filter(team_id=request.user.employee.team_id)
        employee = Employee.objects.get(pk=request.user.employee.id)

        template = 'enrichment_items/enrichment_item_form.html'
        context = {
            "enrichment_item": enrichment_item,
            "enrichment_types": enrichment_types,
            "employee": employee
        }

        return render(request, template, context)

@login_required
def enrichment_item_photo_edit_form(request, enrichment_item_id):

    if request.method == 'GET':

        enrichment_item = EnrichmentItem.objects.get(pk=enrichment_item_id)
        enrichment_types = EnrichmentType.objects.filter(team_id=request.user.employee.team_id)
        employee = Employee.objects.get(pk=request.user.employee.id)

        template = 'enrichment_items/enrichment_item_photo_edit_form.html'
        context = {
            'enrichment_item': enrichment_item,
            'enrichment_types': enrichment_types,
            'employee': employee
        }

        return render(request, template, context)

