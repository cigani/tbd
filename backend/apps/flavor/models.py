import uuid

from django.db import models


# Create your models here.


class Flavor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Flavor Name", max_length=75, default="flavor")
