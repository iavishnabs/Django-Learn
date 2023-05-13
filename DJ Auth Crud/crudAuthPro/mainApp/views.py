from django.shortcuts import render

# Create your views here.

def user_reg(request):
    # sign up form
    
    return render (request,'pages/reg.html')



def index(request):
    # login form 
    return render (request,'index.html')


def userhome(request):
    # after user logged in
    return render (request,'pages/home.html')


