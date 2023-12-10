from django.urls import path
# from current folder import views:
from . import views

# by leaving the first path empty '', this becomes the base url- meaning its the url thats 
# launched initially like a homepage
# index is a function in the views file
app_name = 'foodapp'
urlpatterns = [
    path ('', views.home, name = 'home'),
    path ('about_us/',views.about_us, name = 'about_us'),
    path ('menu/', views.menu, name = 'menu'),
    path ('seafood/', views.seafood, name = 'seafood'),
    path ('meaty/', views.meaty, name = 'meaty'),
    path ('platters/', views.platters, name = 'platters'),

]
