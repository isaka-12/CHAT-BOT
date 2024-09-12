from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
   
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']