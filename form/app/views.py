from django.shortcuts import render
from .form import StudentRegistration
# Create your views here.


def fdata(request):
    fm = StudentRegistration()
    return render(request, 'index.html', {'formdata': fm})

