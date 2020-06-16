from django.db import models
from django.urls import reverse
from .team import Team


class Species(models.Model):

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Species")
        verbose_name_plural = ("Species")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Species_detail", kwargs={"pk": self.pk})
    