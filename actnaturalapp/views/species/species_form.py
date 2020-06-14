from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def species_form(request):
    if request.method == 'GET':

        template = 'species/species_form.html'

        return render(request, template)