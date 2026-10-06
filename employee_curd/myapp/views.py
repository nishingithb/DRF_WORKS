from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from myapp import serializers
from myapp.models import Employee
from myapp.serializers import EmployeeSerializer


# Create your views here.

# APIView for Reading All employee records
class EmployeeList(APIView):
    def get(self,request):
        e=Employee.objects.all()
        #read all employee records from employee table(e)

        serializer_instance=EmployeeSerializer(e,many=True)
        #EmployeeSerializer converts e into python native types
        #e contains more than one record so we use many=True

        return Response(data=serializer_instance.data,status=status.HTTP) #send python native
        #data as json using Response class

# APIView for Reading specific records
class EmployeeDetails(APIView):
    def get(self,request,i):
        # e=Employee.objects.get(id=i)
        e=get_object_or_404(Employee,id=i)
        serializer_instance=EmployeeSerializer(e)
        return Response(data=serializer_instance.data)


class EmployeeCreate(APIView):
    def post(self,request):
        # # data=loads(request.body)
        # data=request.data  #python native type data or dictionary
        #
        # # eid=data['empid']
        # # n=data['name']
        # # a=data['age']
        # # p=data['place']
        # # g=data['gender']
        # # j=data['joining_data']
        # # s=data['salary']
        # # d=data['designation']
        # # e=Employee.objects.create(empid=eid,name=n,age=a,place=p,gender=g,joining_date=j,salary=s,designation=d)
        # e=Employee.objects.create(**data)
        # e.save()
        # return Response({'message':'successful'})


        #view receives data as request.data(client side data -python native type)
        #calls serializer class for deserialization.here we pass request.data as argument
        #after validation serializer saves data as model object inside db table

        serializer_instance=EmployeeSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({'message':'created'})
        else:
            return Response(serializer_instance.errors)


class EmployeeDelete(APIView):
    def delete(self,request,i):
        e=get_object_or_404(Employee,id=i)
        e.delete()
        return Response({'message':'deleted'})


class EmployeeRetrieve(APIView):
    def get(self,request,i):
        e=list(Employee.objects.filter(id=i).values())
        if e:
            return Response(e,safe=False)
        else:
            return Response({'message':'No student data'})



class EmployeeUpdate(APIView):

    def put(self, request, i):
        e=get_object_or_404(Employee,id=i)
        serializer_instance=EmployeeSerializer(e,request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)


class EmployeePatch(APIView):
    def patch(self, request, i):
        e = get_object_or_404(Employee,id=i)
        serializer_instance = EmployeeSerializer(e, request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)