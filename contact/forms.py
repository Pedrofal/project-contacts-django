from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
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
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email', 'description', 'category',
        )
    def clean(self):
        cleaned_data = self.cleaned_data

        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro',
        #         code='invalid'
        #     )
        # )
        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro 2',
        #         code='invalid'
        #     )
        # )

        return super().clean()
    
    # def clean_first_name(self):
    #     first_name = self.cleaned_data.get('first_name')
    #     if   first_name:
    #         self.add_error(
    #         'first_name',
    #         ValidationError(
    #             'fewewfe',
    #             code='invalid'
    #         )
    #     )
    #     return first_name