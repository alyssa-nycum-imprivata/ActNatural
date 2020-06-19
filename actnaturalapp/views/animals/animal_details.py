from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal, Team, Species, Employee, AnimalNote, EnrichmentItem, AnimalEnrichmentItem, EnrichmentLogEntry
from django.contrib.auth.models import User


@login_required
def animal_details(request, animal_id):

    animal = Animal.objects.get(pk=animal_id)
    team = Team.objects.get(pk=animal.team_id)
    species = Species.objects.get(pk=animal.species_id)
    employee = Employee.objects.get(pk=request.user.employee.id)
    notes = AnimalNote.objects.filter(animal_id=animal_id)
    users = User.objects.all()
    animal_enrichment_items = AnimalEnrichmentItem.objects.filter(animal_id=animal_id)
    enrichment_items = EnrichmentItem.objects.all()
    enrichment_log_entries = EnrichmentLogEntry.objects.filter(animal_id=animal_id)

    if request.method == 'GET':

        template = 'animals/animal_details.html'
        context = {
            'animal': animal,
            'team': team,
            'species': species,
            'employee': employee,
            'users': users,
            'notes': notes,
            'animal_enrichment_items': animal_enrichment_items,
            'enrichment_items': enrichment_items,
            'enrichment_log_entries': enrichment_log_entries
        }

        return render(request, template, context)

    elif request.method == 'POST':

        form_data = request.POST
        form_files = request.FILES

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            if (
                "updated_photo" in form_data
            ):

                animal.team_id = request.user.employee.team_id
                animal.species_id = animal.species_id
                animal.name = animal.name
                animal.sex = animal.sex
                animal.age = animal.age
                animal.weight = animal.weight
                animal.image = form_files['image']

                animal.save()

                return redirect(reverse('actnaturalapp:animal', args=[animal.id]))

            else:
                animal.team_id = request.user.employee.team_id
                animal.species_id = form_data['species']
                animal.name = form_data['name']
                animal.sex = form_data['sex']
                animal.age = form_data['age']
                animal.weight = form_data['weight']
                animal.image = animal.image

                animal.save()

                return redirect(reverse('actnaturalapp:animal', args=[animal.id]))
    
        elif (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            
            animal.delete()

            return redirect(reverse('actnaturalapp:animals'))

        else:

            new_note = AnimalNote.objects.create(
                employee_id = request.user.employee.id,
                animal_id = animal_id,
                note = form_data['note'],
                date = form_data['date']
            )

            return redirect(reverse('actnaturalapp:animal', args=[new_note.animal_id]))
