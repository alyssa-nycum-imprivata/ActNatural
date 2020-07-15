import sqlite3
from django.shortcuts import render, redirect, reverse
from ..connection import Connection
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Animal, Species, Employee


@login_required
def animal_list(request, species_id=None):
    
    if request.method == 'GET':

        """GETS all of the species and animal objects associated with the logged in user's team."""

        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            user_employee_id = request.user.employee.id

            db_cursor.execute("""
            SELECT e.id AS 'employee_id',
                e.team_id AS 'employee_team',
                a.id AS 'animal_id',
                a.team_id AS 'animal_team',
                a.name AS 'animal_name',
                a.species_id AS 'animal_species',
                s.id AS 'species_id',
                s.name AS 'species_name',
                s.team_id AS 'species_team'
            FROM actnaturalapp_employee e
            JOIN actnaturalapp_animal a ON e.team_id = a.team_id
            JOIN actnaturalapp_species s ON a.species_id = s.id
            WHERE e.id = ?
            """, (user_employee_id,))

            dataset = db_cursor.fetchall()
            animals = []
            species = []
            
            for row in dataset:
                animal = Animal()
                animal.id = row['animal_id']
                animal.team_id = row['animal_team']
                animal.name = row['animal_name']
                animal.species_id = row['animal_species']
                animals.append(animal)

                specie = Species()
                specie.id = row['species_id']
                specie.team_id = row['species_team']
                specie.name = row['species_name']
                species.append(specie)
            
            # remove duplicate species
            species = set(species)
            species = list(species)

        template = 'animals/animal_list.html'
        context = {
            'animals': animals,
            'species': species,
        }

        return render(request, template, context)

    elif request.method == 'POST':

        form_data = request.POST
        form_files = request.FILES

        if ('age' in form_data):

            """Makes a POST request to add a new animal and then re-directs to that new animal's details page."""

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

                """DELETES a specific species and then re-directs to the animals list page."""

                species.delete()

                return redirect(reverse('actnaturalapp:animals'))

            elif (form_data["actual_method"] == "PUT"):

                """Makes a PUT request to edit a specific species and then re-directs to the animals list page."""

                species.team_id = request.user.employee.team_id
                species.name = form_data['name']

                species.save()

                return redirect(reverse('actnaturalapp:animals'))

        else:

            """Makes a POST request to add a new species and then re-directs to the add animal form."""

            new_species = Species.objects.create(
                team_id = request.user.employee.team_id,
                name = form_data['name']
            )

            return redirect(reverse('actnaturalapp:animal_form'))