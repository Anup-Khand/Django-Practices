from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import Student
# Create your views here.

class studentcreateview(CreateView):
    model = Student
    fields ="__all__"
    success_url = '/list'
    # template_name="myform.html"
 
class studentlistview(ListView):
    model = Student

class studentupdateview(UpdateView):
    model = Student
    fields = "__all__"
    success_url="/list"

class studentdeleteview(DeleteView):
     model = Student
     fields = "__all__"
     success_url="/list"