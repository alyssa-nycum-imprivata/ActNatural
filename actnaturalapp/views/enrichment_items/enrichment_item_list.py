from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import EnrichmentItem


@login_required
def enrichment_item_list(request):

    if request.method == 'GET':

        all_enrichment_items = EnrichmentItem.objects.all()

        template = 'enrichment_items/enrichment_item_list.html'
        context = {
            'all_enrichment_items': all_enrichment_items
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_enrichment_item = EnrichmentItem.objects.create(
            team_id = request.user.employee.team_id,
            name = form_data['name'],
            enrichment_type_id = form_data['enrichment_type'],
            note = form_data['note'],
            is_manager_approved = False,
            is_vet_approved = False,
            image = form_data['image']
        )

        return redirect(reverse('actnaturalapp:enrichment_item', args=[new_enrichment_item.id]))