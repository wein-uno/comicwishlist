# had to create this file, converts model instance in datatypes

from rest_framework import serializers
from .models import Comic  #really love intellisense type

class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = '__all__'  #lots easier than call each one out, not big deal on this small one, but nice
