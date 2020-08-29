from django.urls import path
from .views import *

urlpatterns =[
    path('login/', user_login, name='login'),
    path('signup', user_signup, name='signup'),
    path('logout', user_logout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
    path('profile', user_profile, name='profile'),
    path('profile/create', create_profile, name='create-profile'),
    path('profile/edit', edit_profile, name='edit-profile'),

]