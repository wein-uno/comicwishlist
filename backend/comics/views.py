from django.shortcuts import render

# Create your views here, pull in comic model, and new serializer and dfine the new ComicViewSet
from rest_framework import viewsets
from .models import Comic
from .serializers import ComicSerializer

class ComicViewSet(viewsets.ModelViewSet):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer
