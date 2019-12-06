from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Todo_Serializers
from .models import Todo

# Create your views here.
class Todo_View(viewsets.ModelViewSet):
    serializer_class = Todo_Serializers
    queryset = Todo.objects.all()