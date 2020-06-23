from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal, Species, Employee


@login_required
def animal_form(request):
    if request.method == 'GET':
        
        # grabs the logged in user's employee object
        employee = Employee.objects.get(pk=request.user.employee.id)
        # grabs all of the animals with a team_id that matches the logged in user's team_id
        animals = Animal.objects.filter(team_id=request.user.employee.team_id)
        # grabs all of the species with a team_id that matches the logged in user's team_id
        species = Species.objects.filter(team_id=request.user.employee.team_id)


        template = 'animals/animal_form.html'
        context = {
            'species': species,
            'employee': employee
        }

        return render(request, template, context)

@login_required
def animal_edit_form(request, animal_id):

    # if the animal id exists, grab the specific animal
    # if it doesn't re-direct to the animals list
    try:
        animal = Animal.objects.get(pk=animal_id)
    except:
        return redirect(reverse('actnaturalapp:animals'))

    if request.method == 'GET':

        # if the logged in user's team_id matches the animal's team_id
        if request.user.employee.team_id == animal.team_id:

            # grabs all of the species with the same team_id as the logged in user's team_id
            species = Species.objects.filter(team_id=request.user.employee.team_id)
            # grabs the employee object of the logged in user
            employee = Employee.objects.get(pk=request.user.employee.id)

            template = 'animals/animal_form.html'
            context = {
                'animal': animal,
                'species': species,
                'employee': employee
            }

            return render(request, template, context)

        else:
            # if the logged in user's team_id does not match the animal's team_id, redirect to the animals list
            return redirect(reverse('actnaturalapp:animals'))

@login_required
def animal_photo_edit_form(request, animal_id):

    # if the animal id exists, grab the specific animal
    # if it doesn't re-direct to the animals list
    try:
        animal = Animal.objects.get(pk=animal_id)
    except:
        return redirect(reverse('actnaturalapp:animals'))

    if request.method == 'GET':

        # if the logged in user's team_id matches the animal's team_id
        if request.user.employee.team_id == animal.team_id:

            # grabs all of the species with the same team_id as the logged in user's team_id
            species = Species.objects.filter(team_id=request.user.employee.team_id)
            # grabs the employee object of the logged in user
            employee = Employee.objects.get(pk=request.user.employee.id)

            template = 'animals/animal_photo_edit_form.html'
            context = {
                'animal': animal,
                'species': species,
                'employee': employee
            }

            return render(request, template, context)

        else:
            # if the logged in user's team_id does not match the animal's team_id, redirect to the animals list
            return redirect(reverse('actnaturalapp:animals'))
