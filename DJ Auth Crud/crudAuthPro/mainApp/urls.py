
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('register',views.user_reg,name="user_reg"),
    path('home',views.userhome,name="userhome"),
    
]