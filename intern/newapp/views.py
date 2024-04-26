from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def this_from_second_app(request):
    return HttpResponse("<h2>This is from second app</h2>")

def hello(request):
    return render(request,'a.html',{'name':'basant'})