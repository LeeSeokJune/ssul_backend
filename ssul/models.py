from email.policy import default
from django.db import models
from inheritance.models import TimeStampedModel
from user.models import CustomUser
# Create your models here.


class SsulModel(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.SET_DEFAULT, default=0)
    category = models.CharField(max_length=20, default='기타')
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
