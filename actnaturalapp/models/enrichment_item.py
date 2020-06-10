from django.db import models
from django.urls import reverse
from .team import Team
from .enrichment_type import EnrichmentType


class EnrichmentItem(models.Model):

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    enrichment_type = models.ForeignKey(EnrichmentType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=500)
    is_manager_approved = models.BooleanField()
    is_vet_approved = models.BooleanField()
    image = models.FileField()

    class Meta:
        verbose_name = ("EnrichmentItem")
        verbose_name_plural = ("EnrichmentItems")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("EnrichmentItem_detail", kwargs={"pk": self.pk})
    

