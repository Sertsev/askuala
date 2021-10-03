from django import forms
from django.contrib.auth.models import User
from users.models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

class UserForm(UserCreationForm):

    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    middlename = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Middle name'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'example@example.com'}))
    phonenumber = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'type': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'type': 'password'}))

    class Metal():
        model = User
        fields = ('username', 'firstname', 'middlename', 'lastname', 'email', 'password1', 'password2', 'phonenumber')

        labels = {
            'password1' : 'Password',
            'password2' : 'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):

    student = 'Student'
    teacher = 'Teacher'
    registrar = 'Registrar'
    guest = 'Guest'
    user_types = [
        (student, 'Student'),
        (guest, 'Guest')
    ]

    user_type = forms.ChoiceField(required=True, choices=user_types)

    computerScience = 'Computer Science'
    businessAdmin = 'Business Administration'
    
    Departments = [
        (computerScience, 'Computer Science'),
        (businessAdmin, 'Business Administration')
    ]

    department = forms.ChoiceField(required=True, choices=Departments)

    bsc = 'BSc'
    ba = 'BA'
    ms = 'MS'
    ma = 'MBA'
    programs = [
        (bsc, 'BSc'),
        (ba, 'BA'),
        (ms, 'MS'),
        (ma, 'MBA'),
    ]

    program = forms.ChoiceField(required=True, choices=programs)
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic', 'user_type', 'department', 'program')
