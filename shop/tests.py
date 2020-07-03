from datetime import timedelta

from django.test import TestCase as DjangoTestCase

# Create your tests here.
from django.utils import timezone

from shop.models import ShopUser


class ClientDjangoTest(DjangoTestCase):
    def setUp(self):
        user = ShopUser.object.create(username='elizabeth', )
        user.set_password('password_2020')
        user.save()
        self.user = user
        form_data = {'username': 'elizabeth', 'password': 'password_2020'}
        self.gyg = self.client.post('/signup/', data=form_data)

    def test_create_user_correct(self):
        import pdb
        pdb.set_trace()
        self.client.signup('/')