from turtle import tiltangle, title
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# I will create an endpoint for my api here
# Decorators are used to specify methods that can be accepted e.g GET, POST, PUT

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def song_list(request, format=None):
    
    # get songs
    # return Json
    # serialize them

    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data) 
        
    if request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            

@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, id, format=None):
     
    
    song = Song.objects.get(pk=id)
    
    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)  
    
    # Updating song
    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Deleting song
    elif request.method == 'DELETE':
        # serializer = SongSerializer(song)
        song.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)