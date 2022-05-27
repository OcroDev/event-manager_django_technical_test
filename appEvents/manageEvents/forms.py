from django import forms
from django.contrib.auth import authenticate
from .models import Contact, Events
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    password = forms.CharField(label = 'Passowrd')
    #confirm_password = forms.CharField(label = 'Confirm password')
    class Meta:
        #model = Users
        fields = ('user_name', 'user_email', 'user_password',)
        labels = {'user_name': 'User', 'user_email': 'Email'}

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        #fields = ["name", "email", "bussines_type", "comments", "notify"]
        fields = '__all__'

class addEvent(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['event_name', 'event_date', 'event_description']
        widgets = {
            "event_date" : forms.SelectDateWidget()
        }

class customUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]