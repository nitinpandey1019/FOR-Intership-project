from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django import forms
from .models import Usermodel
class LogInForm(AuthenticationForm):
   username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
   password=forms.CharField(label=("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
