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
    species = Species.objects.get(pk=animal.species_id)
    employee = Employee.objects.get(pk=request.user.employee.id)
    notes = AnimalNote.objects.filter(animal_id=animal_id)
    users = User.objects.all()
    animal_enrichment_items = AnimalEnrichmentItem.objects.filter(animal_id=animal_id)
    enrichment_items = EnrichmentItem.objects.all()
    enrichment_log_entries = EnrichmentLogEntry.objects.filter(animal_id=animal_id)

    enrichment_types = []
    for item in animal_enrichment_items:
        item = item.enrichment_item.enrichment_type.name
        enrichment_types.append(item)

    enrichment_types = set(enrichment_types)
    enrichment_types = list(enrichment_types)

    dates = []
    for date in enrichment_log_entries:
        date = date.date
        dates.append(date)

    dates = set(dates)
    dates = list(dates)

    dates = sorted(dates, key=lambda date:date, reverse=True)

    if request.method == 'GET':

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

        elif ("note" in form_data):

            new_note = AnimalNote.objects.create(
                employee_id = request.user.employee.id,
                animal_id = animal_id,
                note = form_data['note'],
                date = form_data['date']
            )

            return redirect(reverse('actnaturalapp:animal', args=[new_note.animal_id]))

        else:
            selected_enrichment = form_data.getlist('enrichment_items')

            for item in selected_enrichment:
                enrichment_instance = EnrichmentItem.objects.get(pk=item)
                new_animal_enrichment_item = AnimalEnrichmentItem.objects.create(
                    enrichment_item = enrichment_instance,
                    animal = animal
                )

            return redirect(reverse('actnaturalapp:animal', args=[animal.id]))
            

            
