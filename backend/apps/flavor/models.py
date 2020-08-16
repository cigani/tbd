import uuid

from django.db import models
from picklefield.fields import PickledObjectField

# Create your models here.
class Spectrum(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=True, max_length=75)
    data = PickledObjectField(copy=False)


class Flavor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Flavor Name", max_length=75, default="flavor")
    spectrum = models.ForeignKey(
        Spectrum, related_name="flavor", on_delete=models.CASCADE, null=True
    )
