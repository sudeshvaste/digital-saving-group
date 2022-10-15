from dataclasses import fields
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.db import models

class EditUserProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'date_joined', 'last_login']
        labels = {'email':'Email'}


class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username']