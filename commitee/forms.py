from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User, Group
from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.forms import ModelForm

class EditUserProfileForm(ModelForm):
    last_login = None
    date_joined = None
    class Meta:
        model = User
        fields = ['is_active','groups','username','first_name','last_name','email','date_joined','last_login']
        
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['is_active','groups','username','first_name','last_name','email']
        labels = {'groups':'Authority'}

class passwordchangeform(SetPasswordForm):
    class Meta:
        Model = User
        fields = '__all__'

class authorityForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'