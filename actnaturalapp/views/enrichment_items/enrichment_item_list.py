from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import EnrichmentItem, EnrichmentType


@login_required
def enrichment_item_list(request, enrichment_type_id=None):

    if request.method == 'GET':

        enrichment_items = EnrichmentItem.objects.filter(team_id=request.user.employee.team_id)
        enrichment_types = EnrichmentType.objects.all()

        template = 'enrichment_items/enrichment_item_list.html'
        context = {
            'enrichment_items': enrichment_items,
            'enrichment_types': enrichment_types
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        form_files = request.FILES

        if (
            "note" in form_data
        ):

            new_enrichment_item = EnrichmentItem.objects.create(
                team_id = request.user.employee.team_id,
                name = form_data['name'],
                enrichment_type_id = form_data['enrichment_type'],
                note = form_data['note'],
                is_manager_approved = False,
                is_vet_approved = False,
                image = form_files['image']
            )

            return redirect(reverse('actnaturalapp:enrichment_item', args=[new_enrichment_item.id]))

        else:

            new_enrichment_type = EnrichmentType.objects.create(
                name = form_data['name']
            )

            return redirect(reverse('actnaturalapp:enrichment_item_form'))