from django.shortcuts import render
from .models import Film
from .serialization import FilmSort
from rest_framework import serializers, viewsets

# Create your views here.
class FilmView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSort

class Action(viewsets.ModelViewSet):
    queryset = Film.objects.filter(form='action')
    serializer_class = FilmSort

class Comedy(viewsets.ModelViewSet):
    queryset = Film.objects.filter(form = 'comedy')
    serializer_class = FilmSort


class Drama(viewsets.ModelViewSet):
    queryset = Film.objects.filter(form='drama')
    serializer_class = FilmSort

class Fantasy(viewsets.ModelViewSet):
    queryset = Film.objects.filter(form ='fantasy')
    serializer_class = FilmSort

class Horror(viewsets.ModelViewSet):
    queryset = Film.objects.filter(form = 'horror')
    serializer_class = FilmSort

