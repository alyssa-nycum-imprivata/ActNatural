from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal, Team, Species
# from django.core.files.storage import FileSystemStorage

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
        # files = {'media': open(request.files['image'].name, 'rb')}
        # file = request.FILES['filename']
        # form_data = request.POST(file=file)
    

        # myfile = request.FILES['myfile']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)

        form_data = request.POST
        print(form_data)

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            # if form_data['image']:
            #     picture = form_data['image']
            # else:
            #     picture = animal.image

            animal.team_id = request.user.employee.team_id,
            animal.species_id = form_data['species'],
            animal.name = form_data['name'],
            animal.sex = form_data['sex'],
            animal.age = form_data['age'],
            animal.weight = form_data['weight'],
            animal.image = form_data['image']

            animal.save()

            # if form_data.is_valid(): 
            #     form_data.save() 

            return redirect(reverse('actnaturalapp:animal', args=[animal.id]))
    
        elif (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            
            animal.delete()

            return redirect(reverse('actnaturalapp:animals'))
