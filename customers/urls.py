from django.urls import path
# from current folder import views:
from . import views

# by leaving the first path empty '', this becomes the base url- meaning its the url thats 
# launched initially like a homepage
# index is a function in the views file
app_name = 'customers'
urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('register_user/', views.register_user, name = 'register_user'),

]