import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class ShopUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    email_confirmed = models.BooleanField(default=False)
    wallet = models.IntegerField(default=10000)

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
