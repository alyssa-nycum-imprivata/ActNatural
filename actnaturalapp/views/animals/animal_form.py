from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import forms
from actnaturalapp.models import Animal, Species, Employee


@login_required
def animal_form(request):
    if request.method == 'GET':
        
        species = Species.objects.all()
        employee = Employee.objects.get(pk=request.user.employee.id)

        template = 'animals/animal_form.html'
        context = {
            'species': species,
            'employee': employee
        }

        return render(request, template, context)

@login_required
def animal_edit_form(request, animal_id):

    if request.method == 'GET':
        
        animal = Animal.objects.get(pk=animal_id)
        species = Species.objects.all()
        employee = Employee.objects.get(pk=request.user.employee.id)

        template = 'animals/animal_form.html'
        context = {
            'animal': animal,
            'species': species,
            'employee': employee
        }

        return render(request, template, context)