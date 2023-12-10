from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .forms import RegisterUserForm
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'home.html')

# a view for the about us page
def about_us(request):
    return render(request, 'about.html')

# a view for the menu page 
def menu(request):
    return render(request, 'menu.html')

# a view that links to the seafood menu
def seafood(request):
    return render(request, 'seafood.html')

# a view for the link to the meat menu
def meaty(request):
    return render(request, 'meaty.html')

# a view for the platters page
def platters(request):
    return render(request, 'platters.html')

# a view for the login page
# def login_user(request):
#     return render(request, 'authenticate/login.html')

# this method authenticates the user
# authenticate method simply looks up in the Users table and returns an object
# that represents the logged-in user. If the user doesn’t exist in the table(admin), this simply
# returns None. Therefore, let’s send the user back to login if the object is None, and to
# the home page if exists
