from . import views
from django.urls import path

# connect template view 
urlpatterns = [
    path('', views.homePage, name ="homePage"),
    path('about',views.about),
    path('contact',views.contact),
]