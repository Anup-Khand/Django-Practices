from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse
# Create your views here.
def student_api(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': ' data created'}
            return JsonResponse(res.data , safe= False)
    return JsonResponse(serializer.errors)

# get data from 
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data)
    stu = Student.objects.all()
    serializer  = StudentSerializer(stu , many= True)
    return JsonResponse(serializer.data , safe = False)


