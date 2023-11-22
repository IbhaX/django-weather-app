# weather/forms.py
from django import forms

class CityForm(forms.Form):
    city_name = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter City Name", "size": 40}))