from django.db import models
from django.urls import reverse
from .animal import Animal
from .enrichment_item import EnrichmentItem


class AnimalEnrichmentItem(models.Model):

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    enrichment_item = models.ForeignKey(EnrichmentItem, on_delete=models.CASCADE)

    class Meta: 
        verbose_name = ("AnimalEnrichmentItem")
        verbose_name_plural = ("AnimalEnrichmentItems")

    def __str__(self):
        return f'{self.animal.name} {self.enrichment_item.name}'

    def get_absolute_url(self):
        return reverse("AnimalEnrichmentItem_detail", kwargs={"pk": self.pk})
    

