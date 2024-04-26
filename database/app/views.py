from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .utils import Util
# Create your views here.


def index(request):
    # if request.method == "POST":
    #     print("from post request")
    #     name = request.POST.get('username')
    #     em = request.POST.get('email')
    #     pa = request.POST.get('pass')
    #     cp = request.POST.get('cpass')
    #     print(name, em, pa, cp)

    #     if pa != cp:
    #         return HttpResponse("password not correct")
    #     else:
    #         myuser = User.objects.create_user(name, em, pa)
    #         myuser.save()
    #         return redirect('login')

    return render(request, 'base.html')


def login(request):
    if (request.method == "POST"):
        un = request.POST.get('username')
        ps = request.POST.get('pass')
        print(un, ps)
        user = authenticate(request, name=un, pa=un)
        if user is not None:
            login(request, user)
        else:
            return HttpResponse("Username or password doesnot match")

    return render(request, 'login.html')


def h(request):
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
            data = {
                "subject": "Django Mail",
                "body": "You have been registered",
                "to_email": em,
            }
            Util.send_mail(data)

            return redirect('login')

    return render(request, 'h.html')
