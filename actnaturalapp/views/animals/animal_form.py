from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal, Species, Employee


@login_required
def animal_form(request):
    if request.method == 'GET':
        
        employee = Employee.objects.get(pk=request.user.employee.id)
        animals = Animal.objects.filter(team_id=request.user.employee.team_id)
        species = Species.objects.filter(team_id=request.user.employee.team_id)


        template = 'animals/animal_form.html'
        context = {
            'species': species,
            'employee': employee
        }

        return render(request, template, context)

@login_required
def animal_edit_form(request, animal_id):

    try:
        animal = Animal.objects.get(pk=animal_id)
    except:
        return redirect(reverse('actnaturalapp:animals'))

    if request.method == 'GET':

        if request.user.employee.team_id == animal.team_id:

            species = Species.objects.filter(team_id=request.user.employee.team_id)
            employee = Employee.objects.get(pk=request.user.employee.id)

            template = 'animals/animal_form.html'
            context = {
                'animal': animal,
                'species': species,
                'employee': employee
            }

            return render(request, template, context)

        else:
            return redirect(reverse('actnaturalapp:animals'))

@login_required
def animal_photo_edit_form(request, animal_id):

    try:
        animal = Animal.objects.get(pk=animal_id)
    except:
        return redirect(reverse('actnaturalapp:animals'))

    if request.method == 'GET':

        if request.user.employee.team_id == animal.team_id:

            species = Species.objects.filter(team_id=request.user.employee.team_id)
            employee = Employee.objects.get(pk=request.user.employee.id)

            template = 'animals/animal_photo_edit_form.html'
            context = {
                'animal': animal,
                'species': species,
                'employee': employee
            }

            return render(request, template, context)

        else:
            return redirect(reverse('actnaturalapp:animals'))
