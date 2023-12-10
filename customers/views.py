from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
# this method authenticates the user
# authenticate method simply looks up in the Users table and returns an object
# that represents the logged-in user. If the user doesn’t exist in the table(admin), this simply
# returns None. Therefore, let’s send the user back to login if the object is None, and to
# the home page if exists
def login_user(request):
    # if user fills in form:
    if request.method == "POST":
     username = request.POST['username']
     password = request.POST['password']
     # authenticate
     user = authenticate(username=username, password=password)
     if user is not None:
         login(request, user )
         return redirect('foodapp:home')
     else:
         # display login error message
         messages.success(request, ('Error logging in. Try Again.'))
    else:
     return render (request, 'authenticate/login.html',{})
    

# creating a registration view
def register_user(request):
     # if user has filled out the form we pass that post to the UserCreationForm
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        # validating the form: if its been filled out correctly, save the form
        if form.is_valid():
            form.save()
            # upon opening the admin panel, should see the 'registration successfull' message as
            # well as the newly registered user
            # message is displayed on the admin site
            # user is then redirected back to the login page
            messages.success(request, ("Registration successful!"))
            return redirect('customers:login_user') 

    # if the user has not filled in the form yet. Cant use POST because form has not been filled out yet        
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register.html',{
        'form':form,
    })


    
