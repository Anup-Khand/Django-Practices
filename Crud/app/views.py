from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import student
from .forms import studentform

# Create your views here.


def addandshow(request):
    if request.method == 'POST':
        fm = studentform(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            address = fm.cleaned_data['address']
            register = student(name=name, address=address, email=email)
            register.save()
            fm = studentform()
    else:
        fm = studentform()
    stu = student.objects.all()
    return render(request, 'app/addandshow.html', {'form': fm, 'stu': stu})


# delete the user from the database
def delete_data(request, id):
    if request.method == 'POST':
        dt = student.objects.get(pk=id)
        dt.delete()
        return HttpResponseRedirect("/")


# update the user data from the database
def update_data(request, id):
    if request.method == 'POST':
        dt = student.objects.get(pk=id)
        form = studentform(request.POST, instance=dt)
        if form.is_valid():
            form.save()
            return redirect('createandshow')

    else:
        dt = student.objects.get(pk=id)
        form = studentform(instance=dt)
    return render(request, 'app/update_data.html', {'form': form})
