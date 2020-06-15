from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Species


@login_required
def species_form(request):
    if request.method == 'GET':

        template = 'species/species_form.html'

        return render(request, template)

@login_required
def species_edit_form(request, species_id):

    if request.method == 'GET':
        
        species = Species.objects.get(pk=species_id)

        template = 'species/species_form.html'
        context = {
            'species': species
        }

        return render(request, template, context)