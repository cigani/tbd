import uuid

from django.db import models
from picklefield.fields import PickledObjectField
from django.contrib.postgres.fields import JSONField


class Spectrum(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data = JSONField()
    meta = JSONField()


class Flavor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Flavor Name", max_length=75, default="flavor")
    spectrum = models.ForeignKey(
        Spectrum, related_name="flavor", on_delete=models.CASCADE, null=True
    )