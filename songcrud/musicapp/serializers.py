# This describes the process of going from a python object to json

from rest_framework import serializers
from .models import *

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'date_released', 'likes', 'artiste_id']