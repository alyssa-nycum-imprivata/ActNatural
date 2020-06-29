from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from actnaturalapp.models import Employee, Team

@login_required
def home(request):

    employee = Employee.objects.get(pk=request.user.employee.id)
    team = Team.objects.get(pk=request.user.employee.team_id)

    if request.method == 'GET':

        """Gets the logged in user's employee and team info to display on the home page."""

        template = 'home.html'
        context = {
            'employee': employee,
            'team': team
        }

        return render(request, template, context)