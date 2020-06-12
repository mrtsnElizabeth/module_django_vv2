from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from .models import ShopUser


class SignUpForm(UserCreationForm):

    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'date_of_birth',)

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        group = Group.objects.get(name='Users')
        if commit:
            user.save()
            user.groups.add(group)
        return user


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

