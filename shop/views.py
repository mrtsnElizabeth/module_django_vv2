from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.views.generic.base import View

from forms import LoginForm, SignUpForm
from models import ShopUser


class SignupUser(CreateView):
    model = ShopUser
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('home')


@login_required
def home(request):
    return render(request, 'registration/login.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'registration/login.html', {'form': form})


class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(LoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
        return redirect('/')


class LogoutView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        logout(self.request)
        return redirect('/')
