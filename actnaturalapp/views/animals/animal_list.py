from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal, Species, Employee


@login_required
def animal_list(request, species_id=None):
    
    if request.method == 'GET':

        # grabs the logged in user's employee object
        employee = Employee.objects.get(pk=request.user.employee.id)
        # grabs all of the animals that have the same team_id as the logged in user's team_id
        animals = Animal.objects.filter(team_id=request.user.employee.team_id)
        # grabs all of the species that have the same team_id as the logged in user's team_id
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

            # if the 'age' property is included in the form data, post a new animal object from the data typed into the form and then redirect to the new animal's details page

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

            # checks for a hidden input field with name="actual_method"

            # grabs the specific species object
            species = Species.objects.get(pk=species_id)

            if (form_data["actual_method"] == "DELETE"):

                # if the value of the hidden input is "DELETE", delete the specific species and redirect to the animals list

                species.delete()

                return redirect(reverse('actnaturalapp:animals'))

            elif (form_data["actual_method"] == "PUT"):

                # if the value of the hidden input is "PUT", edit the specific species from the data typed into the form and redirect to the animals list

                species.team_id = request.user.employee.team_id
                species.name = form_data['name']

                species.save()

                return redirect(reverse('actnaturalapp:animals'))

        else:

            # if 'age' is not included in the form data and neither is a hidden input field, then create a new species from the data typed into the form and then redirect to the animal form

            new_species = Species.objects.create(
                team_id = request.user.employee.team_id,
                name = form_data['name']
            )

            return redirect(reverse('actnaturalapp:animal_form'))