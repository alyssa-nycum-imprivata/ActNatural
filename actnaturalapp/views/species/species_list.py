from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Species
import ctypes


@login_required
def species_list(request):

    if request.method == 'POST':
        
        form_data = request.POST
        new_species = Species.objects.create(
            name = form_data['name']
        )

        return redirect(reverse('actnaturalapp:animal_form'))
