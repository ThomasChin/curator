from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField("email address", unique=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    nickname = models.CharField(max_length=128, null=True, blank=True)
