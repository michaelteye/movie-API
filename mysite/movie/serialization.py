from django.db import models
from django.db.models import fields
from .models import Film
from rest_framework import serializers

class FilmSort(serializers.ModelSerializer):
    image = serializers.ImageField(max_length = None, use_url = True)

    class Meta:
        model = Film
        fields = ['id','name','description','duration','rating','form', 'image']