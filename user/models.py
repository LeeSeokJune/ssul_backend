from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=20)

    def create(data):
        if CustomUser.exist(data):
            user_object = CustomUser()
            CustomUser.save_object(user_object, data)
        else:
            CustomUser.update(data)

    def update(data):
        user_object = CustomUser.objects.get(username=data['username'])
        CustomUser.save_object(user_object, data)

    def save_object(user_object, data):
        user_object.username = data['username']
        user_object.nickname = data['nickname']
        user_object.set_password(data['password'])
        user_object.save()

    def exist(data):
        try:
            CustomUser.objects.get(username=data['username'])
            return True
        except:
            return False


class SsulCategoryCount(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, default='기타')
    category_count = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def create(data):
        user = CustomUser.objects.get(name=data['name'])
