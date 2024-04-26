from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    Age = serializers.IntegerField()
    City = serializers.CharField(max_length=200)
