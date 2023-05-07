from django.db import models

# Create your models here.

class student_table(models.Model):
    indx_no_field = models.IntegerField()
    name_field = models.CharField(max_length=10)
    place_field = models.CharField(max_length=10)
    course_field = models.CharField(max_length=10)

    def __str__(self):
        return self.name_field