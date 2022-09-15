from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from users.models import UserProfileInfo
from users.forms import  UserProfileInfoForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#number of login attempts limited for fivetimes only
numberofloginattempts = 5


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return HttpResponseRedirect(reverse(page))


def programs(request):
    if not request.user.is_authenticated:
        return render(request, 'programs.html')
    else:
        return HttpResponseRedirect(reverse(page))


# To prevent pages overlapping into one another
page = index

def register(request):
    registered = False
    if not request.user.is_authenticated:
        if request.method == "POST":
            user_form = UserForm(data=request.POST)
            profile_form = UserProfileInfoForm(data=request.POST)

            if profile_form.is_valid() and user_form.is_valid():
                user = user_form.save(commit=False)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                registered = True

            else:
                print(user_form.errors, profile_form.errors) #user_form.errors, 
        else:
            user_form = UserForm()
            profile_form = UserProfileInfoForm()

        return render(request, 'users/register.html',
        {
            'registered':registered,
            'user_form':user_form,
            'profile_form':profile_form}) 
    else:
        return HttpResponseRedirect(reverse(index))

def user_login(request):
    global numberofloginattempts
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:

                    cuser = UserProfileInfo.objects.get(user_id=user.id) # grabbing the current user data from the database
                    
                    global page # global variable to assigne the respective function or page
                    
                    login(request,user)
                    
                    if cuser.user_type == 'Student':
                        page = dashboard
                        return HttpResponseRedirect(reverse(dashboard))
                    elif cuser.user_type == 'Registrar':
                        page = controller
                        return HttpResponseRedirect(reverse(controller))
                    else:
                        return render(request, 'index.html', {
                            'cuser':cuser
                        })
                else:
                    return HttpResponse('Account Deactivated')
            else:
                if numberofloginattempts == 0:
                    numberofloginattempts = 4
                    return HttpResponseRedirect(reverse('index'))
                numberofloginattempts -= 1

                return render(request, 'users/login.html', {
                                                            'user' : user,
                                                            'numberofloginattempts':numberofloginattempts})
        else:
            return render(request, 'users/login.html')
    else:
        return HttpResponseRedirect(reverse(index))

@login_required
def teacher(request):
    cuser = UserProfileInfo.objects.get(user_id=request.user.id)
    alluser = UserProfileInfo.objects.all()

    if request.user.is_authenticated and cuser.user_type == 'Registrar':
        return render(request, 'users/teacher.html', {
        'cuser' : cuser,
        'all' : alluser })
    else:
        return HttpResponseRedirect(reverse(page))

@login_required
def guest(request):
    cuser = UserProfileInfo.objects.get(user_id=request.user.id)
    alluser = UserProfileInfo.objects.all()

    if request.user.is_authenticated and cuser.user_type == 'Registrar':
        return render(request, 'users/guest.html', {
        'cuser' : cuser,
        'all' : alluser })
    else:
        return HttpResponseRedirect(reverse(page))

@login_required
def student(request):
    cuser = UserProfileInfo.objects.get(user_id=request.user.id)
    alluser = UserProfileInfo.objects.all()

    if request.user.is_authenticated and cuser.user_type == 'Registrar':
        return render(request, 'users/student.html', {
        'cuser' : cuser,
        'all' : alluser })
    else:
        return HttpResponseRedirect(reverse(page))


@login_required
def controller(request):
    cuser = UserProfileInfo.objects.get(user_id=request.user.id)
    alluser = UserProfileInfo.objects.all()

    if request.user.is_authenticated and cuser.user_type == 'Registrar':
        return render(request, 'users/controller.html', {
        'cuser' : cuser,
        'all' : alluser })
    else:
        return HttpResponseRedirect(reverse(page))

@login_required
def dashboard(request):
    cuser = UserProfileInfo.objects.get(user_id=request.user.id)
    if request.user.is_authenticated and cuser.user_type == 'Student':
        return render(request, 'users/dashboard.html', {
            'cuser':cuser
        })
    else:
        return HttpResponseRedirect(reverse(page))


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def deactivate(request, cuser, duser):
    if cuser.user_type == 'Registrar':
        if duser.user_type != 'Registrar':
            duser.is_active = False
            return HttpResponse("Deactivated Successefully")
