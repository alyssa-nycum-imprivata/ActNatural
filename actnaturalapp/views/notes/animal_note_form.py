from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal, AnimalNote
import datetime 


@login_required
def animal_note_form(request, animal_id):

    try:
        animal = Animal.objects.get(pk=animal_id)
    except:
        return redirect(reverse('actnaturalapp:animals'))

    if request.method == 'GET':

        """GETS the current date to pre-fill in the add new animal note form."""

        if request.user.employee.team_id == animal.team_id:

            date = str(datetime.date.today())

            template = 'notes/animal_note_form.html'
            context = {
                'animal': animal,
                'date': date
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

        """GETS the details of a specific animal note to pre-fill the edit animal note form."""

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


