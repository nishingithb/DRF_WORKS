from django.db import models

# Create your models here.


class Employee(models.Model):
    empid=models.IntegerField()
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    place=models.CharField(max_length=30)

    gender_choices=[

        ('Male','Male'),('Female','Female')  #(dbvalue,displayvalue)

    ]

    gender=models.CharField(max_length=20,choices=gender_choices)

    # joining_data = models.DateField(auto_now_add=True) #it will add date time automatically

    joining_date=models.DateField()
    salary=models.IntegerField()
    designation=models.CharField(max_length=20)
    image=models.ImageField(upload_to='movies',null=True)

