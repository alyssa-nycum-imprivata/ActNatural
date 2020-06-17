from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import EnrichmentItem



@login_required
def enrichment_item_details(request, enrichment_item_id):

    enrichment_item = EnrichmentItem.objects.get(pk=enrichment_item_id)

    if request.method == 'GET':

        template = 'enrichment_items/enrichment_item_details.html'
        context = {
            "enrichment_item": enrichment_item
        }

        return render(request, template, context)