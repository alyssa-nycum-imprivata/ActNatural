from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal, Team, Species


@login_required
def animal_details(request, animal_id):

    animal = Animal.objects.get(pk=animal_id)
    team = Team.objects.get(pk=animal.team_id)
    species = Species.objects.get(pk=animal.species_id)

    if request.method == 'GET':

        template = 'animals/animal_details.html'
        context = {
            'animal': animal,
            'team': team,
            'species': species
        }
        
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            animal.team_id = request.user.employee.team_id,
            animal.species_id = form_data['species'],
            animal.name = form_data['name'],
            animal.sex = form_data['sex'],
            animal.age = form_data['age'],
            animal.weight = form_data['weight'],
            animal.image = form_data['image']

            animal.save()

            return redirect(reverse('actnaturalapp:animal', args=[animal.id]))
    
        elif (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            
            animal.delete()

            return redirect(reverse('actnaturalapp:animals'))
