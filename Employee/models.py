from django.db import models
 
# table creation
class Department(models.Model):
    dep_name = models.CharField(max_length=30)

    def __str__(self):         #object creation
        return self.dep_name

class Employee(models.Model):
    emp_name =models.CharField(max_length=30)
    dep = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.emp_name 

class mypic(models.Model):
    staff = models.ForeignKey(Employee,on_delete=models.CASCADE)
    image_s = models.ImageField(upload_to='uploads/staffs/',default='')
