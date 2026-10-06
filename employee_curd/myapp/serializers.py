from opcode import i

from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.Serializer):
    empid=serializers.IntegerField()
    name=serializers.CharField(max_length=30)
    age=serializers.IntegerField()
    place=serializers.CharField(max_length=30)

    gender_choices=[

        ('Male','Male'),('Female','Female')  #(dbvalue,displayvalue)

    ]

    gender=serializers.ChoiceField(choices=gender_choices)

    # joining_data = models.DateField(auto_now_add=True) #it will add date time automatically

    joining_date=serializers.DateField()
    salary=serializers.IntegerField()
    designation=serializers.CharField(max_length=20)
    image=serializers.ImageField()

    #after validation and before saving

    def create(self, validated_data):

        e=Employee.objects.create(**validated_data)
        return e  #returns employee object

    def update(self,i,validated_data):
        i.empid=validated_data.get('empid',i.empid)
        i.name=validated_data.get('name',i.name)
        i.age=validated_data.get('age',i.age)
        i.place=validated_data.get('place',i.place)
        i.gender=validated_data.get('gender',i.gender)
        i.joining_date=validated_data.get('joining_date',i.joining_date)
        i.salary=validated_data.get('salary',i.salary)
        i.designation=validated_data.get('designation',i.designation)
        i.save()
        return i

    def validators(self,data):
        if data['age']<=0:
            raise serializers.ValidationError("Age Must be Positive")
        return data