from django.db import models
from inheritance.models import TimeStampedModel
# Create your models here.


class SsulModel(TimeStampedModel):
    order = models.AutoField(primary_key=True)
