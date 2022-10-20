from email.policy import default
from django.db import models
from inheritance.models import TimeStampedModel
# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=20)


class SsulModel(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    # user
    # category
    contents = models.CharField(max_length=1000)
    left_option = models.CharField(max_legth=20)
    left_count = models.IntegerField(default=0)
    right_option = models.CharField(max_legth=20)
    right_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    report_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)


class PopularSsul(TimeStampedModel):
    id = models.AutoField(primary_key=True)
