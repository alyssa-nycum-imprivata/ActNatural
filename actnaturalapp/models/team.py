from django.db import models
from django.urls import reverse


class Team(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Team")
        verbose_name_plural = ("Teams")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Team_detail", kwargs={"pk": self.pk})
    
