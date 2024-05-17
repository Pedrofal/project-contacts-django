from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',
        )
    
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
                },
            ),
        )
    
    first_name = forms.CharField(
       widget=forms.TextInput(
           attrs={
               'placeholder':"First Name",
               }),
        label='First Name'
       )
    last_name = forms.CharField(
       widget=forms.TextInput(
           attrs={
               'placeholder':"Last Name",
               }),
        label='Last Name'
       )
    def clean(self):
        cleaned_data = self.cleaned_data
        return super().clean()
    
class RegisterForm(UserCreationForm):
    ...
    
