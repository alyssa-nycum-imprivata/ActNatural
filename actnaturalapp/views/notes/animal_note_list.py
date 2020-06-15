from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import AnimalNote, Animal, Employee


@login_required
def animal_note_list(request, animal_id):

    employee = Employee.objects.get(pk=request.user.employee.id)
    animal = Animal.objects.get(pk=animal_id)
    notes = AnimalNote.objects.filter(animal_id=animal_id)

    if request.method == 'GET':

        template = 'animals/animal_details.html'
        context = {
            'employee': employee,
            'animal': animal,
            'notes': notes
        }

        return render(request, template, context)