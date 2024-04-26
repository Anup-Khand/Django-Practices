from django.shortcuts import render
from django.views import View
from .models import Student
from .forms import studentform
from django.views.generic import CreateView

# Create your views here.


class studentdata(View):
    name = ""

    def get(self, request):
        print(self.name)
        return render(request, 'index.html')

    def post(self, request):
        print("from the post")
        return render(request, 'new.html')


class Form(View):
    def get(self, request):
        fm = studentform()
        return render(request, 'form.html', {'form': fm})

    def post(self, request):
        fm = studentform(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['email']
            email = fm.cleaned_data['email']
            address = fm.cleaned_data['address']
            register = Student(name=name, address=address, email=email)
            register.save()
            fm = studentform()
        stu = Student.objects.all()
        return render(request, 'form.html', {'form': fm, 'stu': stu})
