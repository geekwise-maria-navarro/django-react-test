from rest_framework import serializers
from .models import Todo


class Todo_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')