from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal, Team, Species, Employee, AnimalNote, EnrichmentItem, AnimalEnrichmentItem, EnrichmentLogEntry, EnrichmentType
from django.contrib.auth.models import User


@login_required
def animal_details(request, animal_id):

    # if the animal id exists, grab the specific animal
    # if it doesn't re-direct to the animals list
    try: 
        animal = Animal.objects.get(pk=animal_id)
    except:
        return redirect(reverse('actnaturalapp:animals'))

    # grabs the team object that matches the specified animal's team_id
    team = Team.objects.get(pk=animal.team_id)
    # grabs the species object that matches the specified animal's species_id
    species = Species.objects.get(pk=animal.species_id)
    # grabs the logged in user's employee object
    employee = Employee.objects.get(pk=request.user.employee.id)
    # grabs all of the notes that have an animal_id that matches the specified animal's id
    notes = AnimalNote.objects.filter(animal_id=animal_id)
    # grabs all of the user objects
    users = User.objects.all()
    # grabs all of the animal enrichment item objects that have the same animal_id as the specified animal's id
    animal_enrichment_items = AnimalEnrichmentItem.objects.filter(animal_id=animal_id)
    # grabs all of the enrichment items
    enrichment_items = EnrichmentItem.objects.all()
    # grabs all of the enrichment log entries that have the same animal_id as the specified animal's id
    enrichment_log_entries = EnrichmentLogEntry.objects.filter(animal_id=animal_id)

    # for each item in animal enrichment item objects, set the item to equal the name of the enrichment type of the enrichment item and then append the item to the enrichment_types list
    enrichment_types = []
    for item in animal_enrichment_items:
        item = item.enrichment_item.enrichment_type.name
        enrichment_types.append(item)

    # this turns the list into a set to remove duplicates
    enrichment_types = set(enrichment_types)
    # this turns the set back into a list so it can be iterated
    enrichment_types = list(enrichment_types)

    # for each entry in the enrichment log entries, set the date equal to the date of the enrichment log entry and then append the date to the dates list
    dates = []
    for date in enrichment_log_entries:
        date = date.date
        dates.append(date)

    # this turns the list into a set to remove duplicates
    dates = set(dates)
    # this turns the set back into a list so it can be iterated
    dates = list(dates)

    # this sorts the dates in the list from most recent to least recent
    dates = sorted(dates, key=lambda date:date, reverse=True)

    if request.method == 'GET':

        # if the logged in user's team_id matches the animals team_id, render the animal's details page
        if request.user.employee.team_id == animal.team_id:

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
                'enrichment_log_entries': enrichment_log_entries,
                'enrichment_types': enrichment_types,
                'dates': dates
            }

            return render(request, template, context)

        else: 
            # if the logged in user's team_id does not match the animal's team_id, redirect to the animals list
            return redirect(reverse('actnaturalapp:animals'))

    elif request.method == 'POST':

        form_data = request.POST
        form_files = request.FILES

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            # if there is a hidden input field where the value is "PUT"

            if (
                "updated_photo" in form_data
            ):

                # if there is also a hidden field with name="updated_photo", then pull the new image path from the form and save it with the rest of the saved animal info, then redirect to the specific animal's details page

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

                # other wise pull all of the animal's edited info from the form and save it, then redirect to the animal's details page
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

            # if there is a hidden input field where the value is "DELETE", then delete the specific animal and redirect to the animals list
                    
            animal.delete()

            return redirect(reverse('actnaturalapp:animals'))

        elif ("note" in form_data):

            # if note is a property in the form_data, then post a new animal note object and redirect to the animal detail's page

            new_note = AnimalNote.objects.create(
                employee_id = request.user.employee.id,
                animal_id = animal_id,
                note = form_data['note'],
                date = form_data['date']
            )

            return redirect(reverse('actnaturalapp:animal', args=[new_note.animal_id]))

        else:

            # grabs all the values from the checkbox inputs with name="enrichment_items" and saves them to the selected_enrichment list
            selected_enrichment = form_data.getlist('enrichment_items')

            # for each item in the selected_enrichment list, make an instance of the enrichment item and then post a new animal enrichment item instance using that item as the enrichment_item and the specified animal as the animal, then redirect the the specified animal's details page
            for item in selected_enrichment:
                enrichment_instance = EnrichmentItem.objects.get(pk=item)
                new_animal_enrichment_item = AnimalEnrichmentItem.objects.create(
                    enrichment_item = enrichment_instance,
                    animal = animal
                )

            return redirect(reverse('actnaturalapp:animal', args=[animal.id]))
            

            
