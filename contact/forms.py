from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',)
    
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={'accept': 'image/*'},
        ),
        required=False,
    )
    
    first_name = forms.CharField(
       widget=forms.TextInput(attrs={'placeholder': "First Name"}),
       label='First Name'
    )
    last_name = forms.CharField(
       widget=forms.TextInput(attrs={'placeholder': "Last Name"}),
       label='Last Name'
    )

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
class RegisterForm(UserCreationForm):
     first_name = forms.CharField(
       widget=forms.TextInput(
           attrs={
               'placeholder':"First Name",
               }),
       required= True
       )
     last_name = forms.CharField(
       widget=forms.TextInput(
           attrs={
               'placeholder':"Last Name",
               }),
       required=True
     )
     email = forms.EmailField(
       widget=forms.EmailInput(
           attrs={
               'placeholder':"Email",
               }),
       required=True, 
     )
     username = forms.CharField(
       widget=forms.TextInput(
           attrs={
               'placeholder':"Username",
               }),
       )
 

     class Meta:
       model = User
       fields = (
           'first_name','last_name','email','username', 
           'password1', 'password2',
                 )
     def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email',ValidationError('Email already exists', code='invalid'))
        return email  
    
    
class RegisterUpdateForm (forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':"First Name",
                }),
        required= True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':"Last Name",
                }),
        required=True,

     )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'auto_complete': 'New Password'
                }),
        required=False,
        label='Password',
        strip=False,
        help_text=password_validation.password_validators_help_text_html,
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password Confirmation',
                'auto_complete': 'New Password'
                }),
        required=False,
        label='Password Confirmation',
        strip=False,
        help_text='Use the same password as before',
    )
    class Meta:
       model = User
       fields = (
           'first_name','last_name','email', 
           )
    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get("password1")
        
        if password:
            user.set_password(password)
        if commit:
            user.save()
            
        return user
        
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 or password2: 
            if password1!= password2:
                self.add_error(
                    'password2', 
                    ValidationError('Passwords do not match', code='invalid')
                    )
        
        return super().clean()
    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        if email!= current_email:
            if User.objects.filter(email=email).exists():
                self.add_error('email',ValidationError('Email already exists', code='invalid'))
        return email
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1', ValidationError(errors))
                
       
        return password1
    