from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from actnaturalapp.models import Employee, Team
from django.forms import ValidationError

# TODO: Need to clean appearance of error messages for registration

def register(request):
    if request.method == 'POST':
        form_data = request.POST
        
        try:
            if form_data['password'] != form_data['password_confirmation']:
                raise ValidationError("Password and password confirmation do not match.")
            
            new_user = User.objects.create_user(
                username=form_data['username'],
                password=form_data['password'],
                email=form_data['email'],
                first_name=form_data['first_name'],
                last_name=form_data['last_name']
            )

            employee = Employee.objects.create(
                team_id=form_data['team'],
                position=form_data['position'],
                user=new_user
            )

            employee.save()
            
            user = authenticate(request, username=form_data['username'], password=form_data['password'])
            if user is not None:
                login(request, user)
                return redirect(reverse('actnaturalapp:home'))
        except Exception as e:
            messages.error(request, e)
                
    teams = Team.objects.all()
    template = 'registration/register.html'
    context = {
        'teams': teams
    }

    return render(request, template, context)