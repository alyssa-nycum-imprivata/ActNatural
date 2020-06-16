from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal, AnimalNote


@login_required
def animal_note_form(request, animal_id):
    if request.method == 'GET':

        animal = Animal.objects.get(pk=animal_id)

        template = 'notes/animal_note_form.html'
        context = {
            'animal': animal
        }

        return render(request, template, context)

@login_required
def animal_note_edit_form(request, note_id):

    if request.method == 'GET':

        note = AnimalNote.objects.get(pk=note_id)
        note.date = str(note.date)

        template = 'notes/animal_note_form.html'
        context = {
            'note': note
        }

        return render(request, template, context)

