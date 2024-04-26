from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Home page</h1>")

def learn_django(request):
    return HttpResponse("welcome")

def learn_templates(request):
    return render(request,'index.html')