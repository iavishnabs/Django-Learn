from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Assignment_status(models.Model):
    status=models.CharField(max_length=20)

    def __str__(self):
        return self.status
    
# extending User model
class user_extend(AbstractUser):
    is_teacher=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Assignments(models.Model):
    orderNo=models.IntegerField()
    name=models.CharField(max_length=20)
    sub=models.CharField(max_length=10)
    img=models.ImageField(upload_to='cover/')
    pdf=models.FileField(upload_to='files/')
    created_by = models.ForeignKey(user_extend,on_delete=models.CASCADE)
    approve = models.BooleanField(default=False)
    reject = models.BooleanField(default=False)
  
    def __str__(self):
        return self.name
    

    
    




