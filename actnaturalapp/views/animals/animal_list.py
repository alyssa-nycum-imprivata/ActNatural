from django.shortcuts import render, redirect, reverse
from actnaturalapp.models import Animal

def animal_list(request):
    
    if request.method == 'GET':

        all_animals = Animal.objects.all()

        template = 'animals/animal_list.html'
        context = {
            'all_animals': all_animals
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

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