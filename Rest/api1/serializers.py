from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    Age = serializers.IntegerField()
    City = serializers.CharField(max_length=200)


def create(self, validate_data):
    return Student.objects.create(**validate_data)
