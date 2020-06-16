# from django.shortcuts import render, redirect, reverse
# from django.contrib.auth.decorators import login_required
# from actnaturalapp.models import Species


# @login_required
# def species_list(request):

#     species = Species.objects.all()

#     if request.method == 'GET':

#         template = 'animals/animal_list.html'
#         context = {
#             'species': species
#         }

#         return render(request, template, context)
