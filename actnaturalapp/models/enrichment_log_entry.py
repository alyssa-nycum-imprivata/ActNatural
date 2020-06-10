from django.db import models
from django.urls import reverse
from .employee import Employee
from .team import Team
from .animal import Animal
from .enrichment_item import EnrichmentItem


class EnrichmentLogEntry(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    enrichment_item = models.ForeignKey(EnrichmentItem, on_delete=models.DO_NOTHING)
    date = models.DateField()
    note = models.CharField(max_length=500)

    class Meta:
        verbose_name = ("EnrichmentLogEntry")
        verbose_name_plural = ("EnrichmentLogEntries")

    def __str__(self):
        return self.note
    
    def get_absolute_url(self):
        return reverse("EnrichmentLogEntry_detail", kwargs={"pk": self.pk})
    