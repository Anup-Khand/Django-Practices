from django.shortcuts import render

# Create your views here.


def Simple_view(request):
    return render(request, 'app1/base.html')
