from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    if request.method == "POST":
        print("from post request")
        name = request.POST.get('username')
        em = request.POST.get('email')
        pa = request.POST.get('pass')
        cp = request.POST.get('cpass')
        print(name, em, pa, cp)

        if pa != cp:
            return HttpResponse("password not correct")
        else:
            myuser = User.objects.create_user(name, em, pa)
            myuser.save()

    return render(request, 'base.html')


def simple_view(request):
    return render(request, 'home.html')


def call(request):
    return render(request, 'Aboutus.html')


def new(request):
    return render(request, 'newpage.html')


def form(request):
    return render(request, 'form.html')
