from django.db import models
from django.contrib.auth.models import AbstractUser, Permission

# Create your models here.


class CustomUser(AbstractUser):

    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.phone_number + self.username

