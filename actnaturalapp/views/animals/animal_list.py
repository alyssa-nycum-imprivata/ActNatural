from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal, Species, Employee


@login_required
def animal_list(request, species_id=None):
    
    if request.method == 'GET':

        employee = Employee.objects.get(pk=request.user.employee.id)
        animals = Animal.objects.filter(team_id=request.user.employee.team_id)
        species = Species.objects.filter(team_id=request.user.employee.team_id)

        template = 'animals/animal_list.html'
        context = {
            'animals': animals,
            'species': species,
            'employee': employee
        }

        return render(request, template, context)

    elif request.method == 'POST':

        form_data = request.POST
        form_files = request.FILES

        if ('age' in form_data):

            new_animal = Animal.objects.create(
                team_id = request.user.employee.team_id,
                species_id = form_data['species'],
                name = form_data['name'],
                sex = form_data['sex'],
                age = form_data['age'],
                weight = form_data['weight'],
                image = form_files['image']
            )

            return redirect(reverse('actnaturalapp:animal', args=[new_animal.id]))

        elif (
            "actual_method" in form_data
        ):

            species = Species.objects.get(pk=species_id)


            if (form_data["actual_method"] == "DELETE"):

                species.delete()

                return redirect(reverse('actnaturalapp:animals'))

            elif (form_data["actual_method"] == "PUT"):

                species.team_id = request.user.employee.team_id
                species.name = form_data['name']

                species.save()

                return redirect(reverse('actnaturalapp:animals'))

        else:

            new_species = Species.objects.create(
                team_id = request.user.employee.team_id,
                name = form_data['name']
            )

            return redirect(reverse('actnaturalapp:animal_form'))