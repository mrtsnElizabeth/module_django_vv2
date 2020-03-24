import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class ShopUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    is_moderator = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    token = models.CharField(max_length=32, unique=True)
    wallet = models.IntegerField(default=10000)

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @staticmethod
    def generate_token():
        return str(uuid.uuid4()).replace('-', '')

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_token()
        return super().save(*args, **kwargs)
