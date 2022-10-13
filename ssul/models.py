from email.policy import default
from django.db import models
from inheritance.models import TimeStampModel
from user.models import UserModel
# Create your models here.


class Category(TimeStampModel):
    name = models.CharField(max_length=10)


class SsulModel(TimeStampModel):
    number = models.AutoField(primary_key=True)
    # user = models.ForeignKey(UserModel, on_delete = models.SET_DEFAULT, default = DEFAULT_MODEL)
    category = models.ForeignKey(Category, )
    contents = models.CharField(max_length=1000, default='')
    left_option = models.CharField(max_length=10)
    left_count = models.IntegerField(default=0)
    right_option = models.CharField(max_length=10)
    left_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    report_count = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
