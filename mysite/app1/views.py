from django.shortcuts import render,redirect
from . models import *

# Create your views here.


# first page -- login & reg here
def index(request):
    table_datas ={
        'studData': student_table.objects.all()
    }
    return render (request,'index.html',table_datas)

# -------------------------------------------------

# after user logged in---go to homepage


def add(request):
    if request.method=="POST":
        index_var = request.POST.get('ind_no')
        name_var = request.POST.get('s_name')
        place_var = request.POST.get('s_place')
        course_var = request.POST.get('s_course')
        ob = student_table(indx_no_field=index_var,name_field=name_var,place_field=place_var,course_field=course_var)
        ob.save()
        return redirect(index)
      
    return render (request,'add.html')

def delete(request,s_id):
    field_del_var = student_table.objects.get(id=s_id)
    field_del_var.delete()
    return redirect(index)
   
def edit(request,s_id):

    field_edit_var = student_table.objects.get(id=s_id)
    if request.method == 'POST':
        index_var = request.POST.get('ind_no')
        name_var = request.POST.get('s_name')
        place_var = request.POST.get('s_place')
        course_var = request.POST.get('s_course')
        student_table.objects.filter(id=s_id).update(indx_no_field=index_var,name_field=name_var,place_field=place_var,course_field=course_var)

        return redirect(index)
    return render (request,'edit.html',{'field_edit_var':field_edit_var})

def home(request):
    
    return render (request,'home.html') 

# -------------------------------------------------
def about(request):
    return render (request,'about.html')

def contact(request):
    return render (request,'contact.html') 