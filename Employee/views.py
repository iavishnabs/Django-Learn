from django.shortcuts import render
from .models import  Employee, mypic

# Create your views here. 
def homePage(request):
    
    display_list = {
        'img': mypic.objects.all(),
        'emp_list' : Employee.objects.all()
    }
    return render(request, 'index.html', display_list)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html') 