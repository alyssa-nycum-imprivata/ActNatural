from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal, Species


@login_required
def animal_list(request, species_id=None):
    
    if request.method == 'GET':

        animals = Animal.objects.all()
        species = Species.objects.all()

        template = 'animals/animal_list.html'
        context = {
            'animals': animals,
            'species': species
        }

        return render(request, template, context)

    elif request.method == 'POST':

        # file = request.FILES['filename']
        # form_data = request.POST(file=file)
        form_data = request.POST

        if ('age' in form_data):

            new_animal = Animal.objects.create(
                team_id = request.user.employee.team_id,
                species_id = form_data['species'],
                name = form_data['name'],
                sex = form_data['sex'],
                age = form_data['age'],
                weight = form_data['weight'],
                image = form_data['image']
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

                species.name = form_data['name']

                species.save()

                return redirect(reverse('actnaturalapp:animals'))

        else:

            new_species = Species.objects.create(
                name = form_data['name']
            )

            return redirect(reverse('actnaturalapp:animal_form'))