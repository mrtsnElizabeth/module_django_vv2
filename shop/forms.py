from django import forms
from django.contrib.auth.forms import UserCreationForm

from views import SignupUser


class SignUpForm(UserCreationForm):

    class Meta:
        model = SignupUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'date_of_birth',)


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

