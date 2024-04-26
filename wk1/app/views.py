from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import Student
# Create your views here


def home(request):
    return render(request, 'base.html')


def Register(request):
    if request.method == "POST":
        print("connected succesfully")
        un = request.POST.get("username")
        em = request.POST.get("email")
        pa = request.POST.get("password")
        cp = request.POST.get("confirm_password")
        print(un, em, pa, cp)
        if pa != cp:
            return HttpResponse("password doesnot match")
        else:
            return redirect("Login")
    return render(request, 'Register.html')


def Login(request):
    if request.method == "POST":
        print("connected succesfully")
        name = request.POST.get("name")
        pas = request.POST.get("pass")
        print(name, pas)
    return render(request, 'Login.html')


def databasedata(request):
    # queryset = Student.objects.filter(roll_no__gt=4):-here gt is greater than and gte is greater than and equal to
    # queryset = Student.objects.filter(name__contains='r'):- contains is used check whether name contain given letter in a word
    # queryset = Student.objects.filter(name__iexact='Krishna'):- here iexact or exact is lookup field
    # queryset = Student.objects.exists():- to check data is available in database
    # queryset = Student.objects.values("name"):- to only display name
    # queryset = Student.objects.order_by("roll_no"):- to order the data
    # '-roll_no' for descending order of roll no
    # '?' for random order of data
    # queryset = Student.objects.exclude(name=value)
    # all() is get all data
    #  queryset = Student.objects.filter(name=value) it is to filter the data
    # startwith='r' is use to filter that start with given letter ,endwith is opposite
    # range(1,3) is display data within range
    queryset = Student.objects.filter(name__startswith='r')
    print(queryset)
    print(queryset.query)
    # print(queryset.query)
    return render(request, 'table.html', {'stu': queryset})
