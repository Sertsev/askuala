from typing import DefaultDict
from django import forms
from django.contrib.auth.models import User
from users.models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

class UserForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'type': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'type': 'password'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'example@example.com'}))

    class Metal():
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        labels = {
            'password1' : 'Password',
            'password2' : 'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    middlename = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Middle name'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    phonenumber = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))

    student = 'Student'
    teacher = 'Teacher'
    registrar = 'Registrar'
    guest = 'Guest'
    user_types = [
        (student, 'Student'),
        (guest, 'Guest')
    ]

    user_type = forms.ChoiceField(required=True, choices=user_types)

    empty = ''
    computerScience = 'Computer Science'
    businessAdmin = 'Business Administration'
    
    Departments = [
        (empty, ''),
        (computerScience, 'Computer Science'),
        (businessAdmin, 'Business Administration')
    ]

    department = forms.ChoiceField(choices=Departments)

    bsc = 'BSc'
    ba = 'BA'
    ms = 'MS'
    ma = 'MBA'
    empty = ''
    programs = [
        (empty, ''),
        (bsc, 'BSc'),
        (ba, 'BA'),
        (ms, 'MS'),
        (ma, 'MBA'),
    ]

    program = forms.ChoiceField(choices=programs)

    class Meta():
        model = UserProfileInfo
        fields = (  'firstname',
                    'middlename',
                    'lastname',
                    'phonenumber',
                    'user_type',
                    'program',
                    'department',
                    'profile_pic')

