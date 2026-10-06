from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.views import APIView
from rest_framework.response import Response
from movies.serializers import MovieSerializer
from .models import Movie

# Create your views here.

# API view for reading all movie record

# class MovieList(APIView):
#     def get(self,request):
#         m=Movie.objects.all()
#         serializer_instance=MovieSerializer(m,many=True)
#         return Response(serializer_instance.data)



# API view for creating new record

# class MovieCreate(APIView):
#     def post(self,request):
#         form_data=request.data
#         serializer_instance=MovieSerializer(data=form_data)
#         if serializer_instance.is_valid():
#
#             # after validation of data
#             # cleaned_data=serializer_instance.validated_data
#             # print(cleaned_data)
#
#             serializer_instance.save()
#             return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance)


# API view for reading specific record

class MoviesCreate(APIView):
    def get(self,request):
        m=Movie.objects.all()
        serializer_instance=MovieSerializer(m,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def post(self, request):
        form_data = request.data
        serializer_instance = MovieSerializer(data=form_data)
        if serializer_instance.is_valid():

            # after validation of data
            # cleaned_data=serializer_instance.validated_data
            # print(cleaned_data)

            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


class MovieRetrieveUpdateDelete(APIView):
    def get(self,request,i):
        m=get_object_or_404(Movie,id=i)
        serialaizer_instance=MovieSerializer(m)
        return Response(serialaizer_instance.data,status=status.HTTP_200_OK)

    def put(self,request,i):
        m=get_object_or_404(Movie,id=i)
        data=request.data
        m.title = data['title']
        m.director = data['director']
        m.language = data['language']
        m.year = data['year']
        m.rating = data['rating']
        m.runtime = data['runtime']
        m.save()
        return Response({'message':'updated'})

    def patch(self,request,i):
        m=get_object_or_404(Movie,id=i)
        data=request.data
        if 'title' in data:
            m.title=data['title']
        if 'director' in data:
            m.director=data['director']
        if 'language' in data:
            m.language=data['language']
        if 'year' in data:
            m.year=data['year']
        if 'rating' in data:
            m.rating=data['rating']
        if 'runtime' in data:
            m.runtime=data['runtime']
        m.save()
        return Response({'message':'partially updated'})

    def delete(self,request,i):
        m=get_object_or_404(Movie,id=i)
        m.delete()
        return Response({'message':'deleted'})
