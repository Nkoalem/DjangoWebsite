from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# editing my Usercreation form so that it includes the following fields
# the RegisterUserForm inherits the UserCreationForm
# this info gets saved into the database
class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email =forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1','password2')