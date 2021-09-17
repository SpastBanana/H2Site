from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput
import datetime


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='',max_length=254, help_text='Required. Inform a valid email address.', widget=TextInput(attrs={'class': 'email','placeholder': 'Email'}))
    username = forms.CharField(label='', widget=TextInput(attrs={'class': 'username','placeholder': 'Gebruikersnaam'}))
    password1 = forms.CharField(label='', widget=PasswordInput(attrs={'class': 'pass-1','placeholder': 'Wachtwoord'}))
    password2 = forms.CharField(label='', widget=PasswordInput(attrs={'class': 'pass-2','placeholder': 'Herhaal wachtwoord'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=TextInput(attrs={'class': 'username','placeholder': 'Gebruikersnaam'}))
    password = forms.CharField(label='', widget=PasswordInput(attrs={'class': 'password','placeholder': 'Wachtwoord'}))