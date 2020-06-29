from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Employee, EnrichmentType, EnrichmentItem, Animal, Species


@login_required
def enrichment_item_form(request):

    if request.method == 'GET':

        """GETS the enrichment type objects and animal objects created by the logged in user's team to populate in the add enrichment item form."""
        
        employee = Employee.objects.get(pk=request.user.employee.id)
        enrichment_types = EnrichmentType.objects.filter(team_id=request.user.employee.team_id)
        animals = Animal.objects.filter(team_id=request.user.employee.team_id)
        species = Species.objects.filter(team_id=request.user.employee.team_id)

        template = 'enrichment_items/enrichment_item_form.html'
        context = {
            'enrichment_types': enrichment_types,
            'employee': employee,
            'animals': animals,
            'species': species
        }

        return render(request, template, context)

@login_required
def enrichment_item_edit_form(request, enrichment_item_id):

    try: 
        enrichment_item = EnrichmentItem.objects.get(pk=enrichment_item_id)
    except:
        return redirect(reverse('actnaturalapp:enrichment_items'))

    
    if request.method == 'GET':

        """GETS the details of a specific enrichment item to pre-fill the edit enrichment item form."""

        if request.user.employee.team_id == enrichment_item.team_id:

            enrichment_types = EnrichmentType.objects.filter(team_id=request.user.employee.team_id)
            animals = Animal.objects.filter(team_id=request.user.employee.team_id)
            species = Species.objects.filter(team_id=request.user.employee.team_id)
            employee = Employee.objects.get(pk=request.user.employee.id)

            template = 'enrichment_items/enrichment_item_form.html'
            context = {
                'enrichment_item': enrichment_item,
                'enrichment_types': enrichment_types,
                'employee': employee,
                'animals': animals,
                'species': species
            }

            return render(request, template, context)

        else:
            return redirect(reverse('actnaturalapp:enrichment_items'))


@login_required
def enrichment_item_photo_edit_form(request, enrichment_item_id):

    try: 
        enrichment_item = EnrichmentItem.objects.get(pk=enrichment_item_id)
    except:
        return redirect(reverse('actnaturalapp:enrichment_items'))

    if request.method == 'GET':

        """GETS the details of a specific enrichment item for the edit photo form."""

        if request.user.employee.team_id == enrichment_item.team_id:

            enrichment_types = EnrichmentType.objects.filter(team_id=request.user.employee.team_id)
            animals = Animal.objects.filter(team_id=request.user.employee.team_id)
            species = Species.objects.filter(team_id=request.user.employee.team_id)
            employee = Employee.objects.get(pk=request.user.employee.id)

            template = 'enrichment_items/enrichment_item_photo_edit_form.html'
            context = {
                'enrichment_item': enrichment_item,
                'enrichment_types': enrichment_types,
                'employee': employee,
                'animals': animals,
                'species': species
            }

            return render(request, template, context)

        else:
            return redirect(reverse('actnaturalapp:enrichment_items'))


