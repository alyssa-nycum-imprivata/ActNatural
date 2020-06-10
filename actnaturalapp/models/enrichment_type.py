from django.db import models
from django.urls import reverse


class EnrichmentType(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("EnrichmentType")
        verbose_name_plural = ("EnrichmentTypes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("EnrichmentType_detail", kwargs={"pk": self.pk})
    