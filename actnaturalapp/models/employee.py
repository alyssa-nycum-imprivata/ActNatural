from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .team import Team


class Employee(models.Model):
    
    user = models.OneToOneField(User, related_name='employee', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})
    