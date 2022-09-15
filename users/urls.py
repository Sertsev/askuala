from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('programs/', views.programs, name='programs'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('controller/', views.controller, name='controller'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    path('guest/', views.guest, name='guest'),
]

