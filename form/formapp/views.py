from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .form import StudentRegistration,FormRegistration
# Create your views here.

def data(request):
    return render(request,'data.html')

def fdata(request):
    fm = StudentRegistration()
    return render(request, 'form.html', {'formdata': fm})

def postform(request):
    if request.method == "POST":
        fm = FormRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            print(name,email)
            return HttpResponseRedirect('/sucess')
            # return render(request,'data.html',{'name':name,'email':email})
    else:
        fm = FormRegistration()
    return render(request,'postform.html',{'formdata':fm})

