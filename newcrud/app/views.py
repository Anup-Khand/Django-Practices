from django.shortcuts import render, HttpResponseRedirect
from .forms import UserForm
from .models import UserMod
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


def add_show(request):
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pa = fm.cleaned_data['password']
            epa = make_password(pa)
            # It can save individual field
            reg = UserMod(name=nm, email=em, password=epa)
            reg.save()
           # Or fm.save()   #It save all field at once
    else:
        fm = UserForm()
    stud = UserMod.objects.all()  # Retrieve all data from the database
    return render(request, 'addandshow.html', {'form': fm, 'data': stud})


def delete_data(request, id):
    if request.method == 'POST':
        fm = UserMod.objects.get(pk=id)
        fm.delete()
        return HttpResponseRedirect('/')


def update_data(request, id):
    if request.method == "POST":
        pi = UserMod.objects.get(pk=id)
        fm = UserForm(request.POST, instance=pi)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pa = fm.cleaned_data['password']
            epa = make_password(pa)
            pi.name = nm
            pi.email = em
            pi.password = epa
            pi.save()
    else:
        pi = UserMod.objects.get(pk=id)
        fm = UserForm(instance=pi)
    return render(request, 'update.html', {"form": fm})



