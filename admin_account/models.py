# admin_account/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class AdminAccount(AbstractUser):
    # phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
