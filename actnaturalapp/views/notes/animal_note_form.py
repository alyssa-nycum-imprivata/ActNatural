from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal


@login_required
def animal_note_form(request, animal_id):
    if request.method == 'GET':

        animal = Animal.objects.get(pk=animal_id)

        template = 'notes/animal_note_form.html'
        context = {
            'animal': animal
        }

        return render(request, template, context)

