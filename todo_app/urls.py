
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   path('' , home , name='home' ), 
   path('login/' ,login  , name='login'), 
   path('signup/' , signup ), 
   path('add-todo/' , add_todo ), 
   path('delete-todo/<int:id>' , delete_todo ), 
   path('logout/' , signout ), 
   path('change-status/<int:id>/<str:jarayon>' , change_todo ),
   
]
