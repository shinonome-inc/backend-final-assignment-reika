from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    email = models.EmailField()
    groups = models.ManyToManyField(Group, related_name="custom_user_set", blank=True)  # related_nameを追加
    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_user_permissions_set", blank=True  # related_nameを追加
    )
