from django.db import models
from django.urls import reverse
from .team import Team
from .species import Species


class Animal(models.Model):

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    weight = models.IntegerField()
    image = models.ImageField(upload_to="media/", null=True, blank=True)

    class Meta:
        verbose_name = ("Animal")
        verbose_name_plural = ("Animals")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Animal_detail", kwargs={"pk": self.pk})
    