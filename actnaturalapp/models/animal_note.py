from django.db import models
from django.urls import reverse
from .employee import Employee
from .team import Team
from .animal import Animal

class AnimalNote(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    note = models.CharField(max_length=500)
    date = models.DateField()

    class Meta:
        verbose_name = ("AnimalNote")
        verbose_name_plural = ("AnimalNotes")

    def __str__(self):
        return self.note

    def get_absolute_url(self):
        return reverse("AnimalNote_detail", kwargs={"pk": self.pk})
    