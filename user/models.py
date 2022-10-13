from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserModel(AbstractUser):
    nickname = models.CharField(max_length=20)
    # category = models.CharField

# username, first_name, last_name, email,password, groups, user_permission, is_staff, is_active, is_super_user,last_login,date_joined
