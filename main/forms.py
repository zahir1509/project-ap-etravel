from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class Rateform(forms.ModelForm):
    text = forms.CharField(widget = forms.Textarea(attrs ={'class': 'materialize-textarea'}), required= False)
    rate = forms.ChoiceField(choices= RATE_CHOICES, widget= forms.Select(), required= True)
    class Meta:
        model = Review
        fields = ('text', 'rate')