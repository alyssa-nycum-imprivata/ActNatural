from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Employee, EnrichmentType


@login_required
def enrichment_item_form(request):
    if request.method == 'GET':
        
        # employee = Employee.objects.get(pk=request.user.employee.id)
        enrichment_types = EnrichmentType.objects.all()

        template = 'enrichment_items/enrichment_item_form.html'
        context = {
            'enrichment_types': enrichment_types
        }

        return render(request, template, context)