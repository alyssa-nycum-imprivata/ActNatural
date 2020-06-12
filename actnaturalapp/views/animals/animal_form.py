from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import forms
from actnaturalapp.models import Animal, Species, Employee


# class AnimalForm(forms.ModelForm):

#     class Meta:
#         model = Animal
#         fields = ['team', 'species', 'name', 'sex', 'age', 'weight', 'image']

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

# @login_required
# def animal_edit_form(request, book_id):

#     if request.method == 'GET':
#         book = get_book(book_id)
#         libraries = get_libraries()

#         template = 'books/form.html'
#         context = {
#             'book': book,
#             'all_libraries': libraries
#         }

#         return render(request, template, context)