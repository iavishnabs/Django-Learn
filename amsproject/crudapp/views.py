from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import os
from . models import *

# Create your views here.

def home(request):
    return render(request,'home.html')

@login_required
def show(request):
    d={
        'users_dis': Assignments.objects.filter(created_by=request.user),
        'dis_all':Assignments.objects.all()
    }
    return render(request,'view.html',d)


@login_required
def add(request):
    if request.user.is_authenticated:
       if request.method == "POST":
          i=request.POST.get('index')
          n=request.POST.get('fname')
          s=request.POST.get('subject')
          c=request.FILES['mycover']
          f=request.FILES['myfile']

          obj = Assignments(orderNo=i,name=n,sub=s,img=c,pdf=f,created_by=request.user)
          obj.save()
          return redirect(home)
    return render(request,'add.html')

def remove(request,aid):
    item = Assignments.objects.get(id=aid)
    item.delete()
    return redirect(show)
    
@login_required
def edit(request,aid):
    im = Assignments.objects.get(id=aid)

    if request.method == "POST":
        if "img" in request.FILES and "pdf" in request.FILES:
            os.remove(im.img.path)
            os.remove(im.pdf.path)
            im.img=request.FILES['mycover']
            im.pdf=request.FILES['myfile']
        indxno=request.POST.get('ord')   
        name=request.POST.get('usname')
        subj=request.POST.get('subj')
        ap = request.POST.get('appr') == "on"
        rej = request.POST.get('rej') == "on"
        
        obj=Assignments.objects.filter(id=aid).update(orderNo=indxno,name=name,sub=subj)
        print("updated!!!!!!!") 
        if request.user.is_teacher:
            if ap:
                im.approve = True
            elif rej:
                im.reject= True
        im.save()
        return redirect(show)
    return render(request,'edit.html',{'im':im})

   
def Signup(request):
    #  pswd emailid  tch std
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        if request.method == "POST":
            u = request.POST.get('uname')
            psw = request.POST.get('pswd')
            em = request.POST.get('emailid')
            no = request.POST.get('phn')
            is_tch = request.POST.get('tch') == "on"
            is_std = request.POST.get('std') == "on"

            if user_extend.objects.filter(username=u,email=em).exists():
                print("already have this user")
                return redirect(home)
            else:
                new=user_extend.objects.create_user(u,em,psw)
                new.phn = no
                if is_tch:
                    new.is_teacher=True
                else:
                    new.is_student=True
                new.save()
                return redirect(userlogin)
    return render(request,'users/reg.html')

def userlogin(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        if request.method == "POST":
            u = request.POST.get('uname')
            psw=request.POST.get('pswd')

            us = authenticate(request,username=u,password=psw)
            if us is not None:
                login(request,us)
                return redirect(home)
            else:
                print("user not exist")
                return redirect(userlogin)

    return render(request,'users/login.html') 

@login_required
def logoutuser(request):
    logout(request)
    return redirect(userlogin)