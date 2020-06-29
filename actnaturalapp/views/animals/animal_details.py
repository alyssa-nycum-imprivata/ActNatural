from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal, Team, Species, Employee, AnimalNote, EnrichmentItem, AnimalEnrichmentItem, EnrichmentLogEntry, EnrichmentType
from django.contrib.auth.models import User


@login_required
def animal_details(request, animal_id):

    try: 
        animal = Animal.objects.get(pk=animal_id)
    except:
        return redirect(reverse('actnaturalapp:animals'))

    team = Team.objects.get(pk=animal.team_id)
    employee = Employee.objects.get(pk=request.user.employee.id)
    users = User.objects.all()

    notes = AnimalNote.objects.filter(animal_id=animal_id)
    enrichment_log_entries = EnrichmentLogEntry.objects.filter(animal_id=animal_id)

    species = Species.objects.get(pk=animal.species_id)
    all_animal_enrichment_items = AnimalEnrichmentItem.objects.filter(animal_id=animal_id)
    enrichment_items = EnrichmentItem.objects.all()

    # sorts the approved and unapproved animal enrichment items into separate lists
    approved_animal_enrichment_items = []
    unapproved_animal_enrichment_items = []
    for item in all_animal_enrichment_items:
        if (item.is_manager_approved == True & item.is_vet_approved == True):
            approved_animal_enrichment_items.append(item)
        else:
            unapproved_animal_enrichment_items.append(item)

    # grabs the associated enrichment type object for each approved animal enrichment item
    enrichment_types = []
    for item in approved_animal_enrichment_items:
        item = item.enrichment_item.enrichment_type.name
        enrichment_types.append(item)

    # gets a unique list of those enrichment type objects
    enrichment_types = set(enrichment_types)
    enrichment_types = list(enrichment_types)

    # grabs the date of each enrichment log entry
    dates = []
    for date in enrichment_log_entries:
        date = date.date
        dates.append(date)

    # gets a unique list of those dates
    dates = set(dates)
    dates = list(dates)

    # sorts the dates from most recent to least recent
    dates = sorted(dates, key=lambda date:date, reverse=True)

    if request.method == 'GET':

        """GETS all of a specific animal's details, notes, approved animal enrichment items, and enrichment log entries."""

        if request.user.employee.team_id == animal.team_id:

            template = 'animals/animal_details.html'
            context = {
                'animal': animal,
                'team': team,
                'species': species,
                'employee': employee,
                'users': users,
                'notes': notes,
                'approved_animal_enrichment_items': approved_animal_enrichment_items,
                'enrichment_items': enrichment_items,
                'enrichment_log_entries': enrichment_log_entries,
                'enrichment_types': enrichment_types,
                'dates': dates
            }

            return render(request, template, context)

        else: 
            return redirect(reverse('actnaturalapp:animals'))

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

                """Makes a PUT request to edit a specific animal's image and then re-directs to the animal's details page."""

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

                """Makes a PUT request to edit a specific animal's details and then re-directs to the animal's details page."""

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

            """DELETES a specific animal and then re-directs to the animals list."""
                    
            animal.delete()

            return redirect(reverse('actnaturalapp:animals'))

        elif ("note" in form_data):

            """Makes a POST request to add a new note to a specific animal and then re-directs to the animal's details page."""

            new_note = AnimalNote.objects.create(
                employee_id = request.user.employee.id,
                animal_id = animal_id,
                note = form_data['note'],
                date = form_data['date']
            )

            return redirect(reverse('actnaturalapp:animal', args=[new_note.animal_id]))

        else:

            """Gets the values from the selected checkboxes and makes a POST request for each animal enrichment item object that the user selected to get approved for a specific animal, then re-directs to the items pending approval page for the animal."""

            selected_enrichment = form_data.getlist('enrichment_items')

            for item in selected_enrichment:
                enrichment_instance = EnrichmentItem.objects.get(pk=item)
                new_animal_enrichment_item = AnimalEnrichmentItem.objects.create(
                    enrichment_item = enrichment_instance,
                    animal = animal,
                    is_manager_approved = False,
                    is_vet_approved = False
                )

            return redirect(reverse('actnaturalapp:animal_enrichment_items_waiting_approval', args=[animal.id]))

@login_required
def animal_enrichment_items_waiting_approval(request, animal_id):
    
    try: 
        animal = Animal.objects.get(pk=animal_id)
    except:
        return redirect(reverse('actnaturalapp:animals'))

    team = Team.objects.get(pk=animal.team_id)
    employee = Employee.objects.get(pk=request.user.employee.id)
    users = User.objects.all()

    notes = AnimalNote.objects.filter(animal_id=animal_id)
    enrichment_log_entries = EnrichmentLogEntry.objects.filter(animal_id=animal_id)

    species = Species.objects.get(pk=animal.species_id)
    all_animal_enrichment_items = AnimalEnrichmentItem.objects.filter(animal_id=animal_id)
    enrichment_items = EnrichmentItem.objects.all()

    # sorts the approved and unapproved animal enrichment items into separate lists
    approved_animal_enrichment_items = []
    unapproved_animal_enrichment_items = []
    for item in all_animal_enrichment_items:
        if (item.is_manager_approved == True & item.is_vet_approved == True):
            approved_animal_enrichment_items.append(item)
        else:
            unapproved_animal_enrichment_items.append(item)

    # grabs the associated enrichment type object for each approved animal enrichment item
    enrichment_types = []
    for item in unapproved_animal_enrichment_items:
        item = item.enrichment_item.enrichment_type.name
        enrichment_types.append(item)

    # gets a unique list of those enrichment type objects
    enrichment_types = set(enrichment_types)
    enrichment_types = list(enrichment_types)   

    if request.method == 'GET':

        """GETS all of a specific animal's submitted unapproved animal enrichment items."""

        if request.user.employee.team_id == animal.team_id:

            template = 'animals/animal_enrichment_items_waiting_approval.html'
            context = {
                'animal': animal,
                'team': team,
                'species': species,
                'employee': employee,
                'users': users,
                'notes': notes,
                'unapproved_animal_enrichment_items': unapproved_animal_enrichment_items,
                'enrichment_items': enrichment_items,
                'enrichment_log_entries': enrichment_log_entries,
                'enrichment_types': enrichment_types
            }

            return render(request, template, context)

        else: 
            return redirect(reverse('actnaturalapp:animals'))
