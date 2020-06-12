from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal, Species


@login_required
def animal_list(request):
    
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
        print(request)

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