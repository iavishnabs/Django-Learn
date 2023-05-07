
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.add,name='add'),
    path('delete/<int:s_id>',views.delete,name='delete'),
    path('edit/<int:s_id>',views.edit,name='edit'),

    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
]