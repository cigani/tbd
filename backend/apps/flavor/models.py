import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models


class Flavor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    additive = models.CharField(verbose_name="Additive", max_length=75, null=True)
    substrate = models.CharField(verbose_name="Substrate", max_length=75, null=True)
    pdms = models.CharField(
        verbose_name="PDMS", null=True, blank=True, max_length=50
    )
    lims = models.CharField(
        verbose_name="LIMS", null=True, blank=True, max_length=50)


class Spectrum(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(blank=True, default="")
    data = JSONField(null=True)
    meta = JSONField(null=True)
    flavor = models.ForeignKey(
        Flavor, related_name="spectrum", on_delete=models.CASCADE, null=True
    )
    ions = JSONField(blank=True, null=True)
    pure = models.BooleanField(default=False)
    formulation = models.CharField(blank=True, default="", max_length=1000)
    image = models.FileField(null=True)
