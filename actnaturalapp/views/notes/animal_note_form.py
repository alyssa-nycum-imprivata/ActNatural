from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal, AnimalNote


@login_required
def animal_note_form(request, animal_id):

    try:
        animal = Animal.objects.get(pk=animal_id)
    except:
        return redirect(reverse('actnaturalapp:animals'))

    if request.method == 'GET':

        if request.user.employee.team_id == animal.team_id:

            template = 'notes/animal_note_form.html'
            context = {
                'animal': animal
            }

            return render(request, template, context)

        else:
            return redirect(reverse('actnaturalapp:animals'))
            
@login_required
def animal_note_edit_form(request, note_id):

    try: 
        note = AnimalNote.objects.get(pk=note_id)
    except:
        return redirect(reverse('actnaturalapp:animals'))

    if request.method == 'GET':

        if request.user.employee.id == note.employee_id:

            note = AnimalNote.objects.get(pk=note_id)
            note.date = str(note.date)

            template = 'notes/animal_note_form.html'
            context = {
                'note': note
            }

            return render(request, template, context)

        else:
            return redirect(reverse('actnaturalapp:animals'))


