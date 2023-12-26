from django import forms
from .models import *


class DestinationRegister(forms.ModelForm):
    destination_name = forms.CharField(widget=forms.TextInput)
    description = forms.CharField(widget=forms.TextInput)
    location = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Destinations
        fields = ['destination_name', 'description', 'location']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    date_of_birth = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'firstname', 'lastname', 'date_of_birth', 'contact_number']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class AddReview(forms.Form):
    username = forms.CharField(max_length=20)
    rating = forms.IntegerField()
    comment = forms.CharField(max_length=200)

