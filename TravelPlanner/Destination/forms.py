from django import forms
from .models import Destinations


class DestinationRegister(forms.ModelForm):
    destination_name = forms.CharField(widget=forms.TextInput)
    description = forms.CharField(widget=forms.TextInput)
    location = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Destinations
        fields = ['destination_name', 'description', 'location']
