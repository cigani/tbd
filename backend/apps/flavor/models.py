import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models


class Spectrum(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data = JSONField(null=True)
    meta = JSONField(null=True)
    pure = models.BooleanField(verbose_name="Pure Compound", default=False, null=True)


class Flavor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    additive = models.CharField(verbose_name="Additive", max_length=75, null=True)
    substrate = models.CharField(verbose_name="Substrate", max_length=75, null=True)
    spectrum = models.ForeignKey(
        Spectrum, related_name="flavor", on_delete=models.CASCADE, null=True
    )
    pure = JSONField(null=True)
