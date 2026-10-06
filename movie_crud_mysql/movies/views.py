from django.db.migrations import CreateModel
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from rest_framework import status, generics
from rest_framework.mixins import CreateModelMixin
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

# class MoviesCreate(APIView):
# def get(self,request):
#     m=Movie.objects.all()
#     serializer_instance=MovieSerializer(m,many=True)
#     return Response(serializer_instance.data,status=status.HTTP_200_OK)
#
# def post(self, request):
#     form_data = request.data
#     serializer_instance = MovieSerializer(data=form_data)
#     if serializer_instance.is_valid():
#
#         # after validation of data
#         # cleaned_data=serializer_instance.validated_data
#         # print(cleaned_data)
#
#         serializer_instance.save()
#         return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

# from rest_framework import mixins,generics

# class MovieListCreate(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
# class MovieRetrieveUpdateDelete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#
#     def put(self,request,pk):
#         return self.update(request,pk)
#
#     def patch(self,request,pk):
#         return self.partial_update(request,pk)
#
#     def delete(self,request,pk):
#         return self.destroy(request,pk)

# class MovieListCreate(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
# class MovieRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


# class MovieRetrieveUpdateDelete(APIView):
#     def get(self,request,i):
#         m=get_object_or_404(Movie,id=i)
#         serialaizer_instance=MovieSerializer(m)
#         return Response(serialaizer_instance.data,status=status.HTTP_200_OK)
#
#     def put(self,request,i):
#         m=get_object_or_404(Movie,id=i)
#         data=request.data
#         m.title = data['title']
#         m.director = data['director']
#         m.language = data['language']
#         m.year = data['year']
#         m.rating = data['rating']
#         m.runtime = data['runtime']
#         m.save()
#         return Response({'message':'updated'})
#
#     def patch(self,request,i):
#         m=get_object_or_404(Movie,id=i)
#         data=request.data
#         if 'title' in data:
#             m.title=data['title']
#         if 'director' in data:
#             m.director=data['director']
#         if 'language' in data:
#             m.language=data['language']
#         if 'year' in data:
#             m.year=data['year']
#         if 'rating' in data:
#             m.rating=data['rating']
#         if 'runtime' in data:
#             m.runtime=data['runtime']
#         m.save()
#         return Response({'message':'partially updated'})
#
#     def delete(self,request,i):
#         m=get_object_or_404(Movie,id=i)
#         m.delete()
#         return Response({'message':'deleted'})


# VIEWSETS
from rest_framework import viewsets


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# search API View
from django.db.models import Q

class SearchAPIView(APIView):
    def get(self, request):
        data = self.request.query_params.get('search')

        m = Movie.objects.filter(
            Q(title__icontains=data) |
            Q(director__icontains=data))

        if not m.exists():
            return Response({'message': 'no Record Found'},status=status.HTTP_200_OK)

        serializer_instance = MovieSerializer(m, many=True)

        return Response(serializer_instance.data,status=status.HTTP_200_OK)

from rest_framework.filters import SearchFilter

class SearchAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'director', 'language']


class RegisterAPIView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)

        else:

            return Response(serializer_instance.data,status=status.HTTP_400_BAD_REQUEST)
