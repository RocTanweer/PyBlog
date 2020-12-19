from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    #extra field in the form 
    email = forms.EmailField()

    class Meta:
        #model that will be affected by this form
        model = User
        #fields to show in form
        fields = ['username', 'email', 'password1', 'password2']