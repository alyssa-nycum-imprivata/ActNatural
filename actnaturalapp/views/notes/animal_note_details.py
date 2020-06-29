from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import AnimalNote, Animal


@login_required
def animal_note_details(request, note_id):

    note = AnimalNote.objects.get(pk=note_id)
    animal = Animal.objects.get(pk=note.animal_id)

    if request.method == 'POST':

        form_data = request.POST

        if (
            "actual_method" in form_data and form_data["actual_method"] == "DELETE"
        ):

            """DELETES a specific animal note and then re-directs to the animal details page of the animal associated with that note."""

            note.delete()

            return redirect(reverse('actnaturalapp:animal', args=[animal.id]))

        elif (
            "actual_method" in form_data and form_data["actual_method"] == "PUT"
        ):

            """Makes a PUT request to edit a specific animal note and then re-directs to the animal details page of the animal associated with that note."""

            note.employee_id = request.user.employee.id
            note.animal_id = animal.id
            note.date = form_data["date"]
            note.note = form_data["note"]

            note.save()

            return redirect(reverse('actnaturalapp:animal', args=[animal.id]))
