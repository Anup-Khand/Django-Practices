from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.


def setCookie(request):
    response = render(request, 'setCookie.html')
    response.set_cookie(
        'name', 'sonam', max_age=120)
    return response


def getCookie(request):
    name = request.COOKIES['name']
    # this method helps to set default value of cookies i.e Guest if cookies is not av ialable
    # name = request.COOKIES.get('name', "this is default")
    return render(request, 'getCookies.html', {'name': name})


def delcookie(request):
    response = render(request, 'delCookie.html')
    response.delete_cookie('name')
    return response
