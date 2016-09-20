from django.shortcuts import render
from rest_framework import viewsets, serializers

from drf_app.models import Author

# Create your views here.


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
