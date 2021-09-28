from django import forms
from django.contrib.auth.models import User
from users.models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Metal():
        model = User
        fields = ('username', 'firstname', 'lastname', 'email', 'password1', 'password2', 'phonenumber', 'location', 'dateofbirth')

        labels = {
            'password1' : 'Password',
            'password2' : 'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):

    batch = forms.DateField(required=True)

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
        fields = ('batch', 'profile_pic', 'user_type', 'department', 'program')
