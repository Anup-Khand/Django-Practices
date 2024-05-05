from email.policy import default
from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = "sonam"
    request.session['lname'] = "jsh"
    return render(request,'setsession.html')

def getsession(request):
    name = request.session['name']
    lname = request.session.get('lname',default="hrrrlo")
    age = request.session.setdefault('age','26')
    return render(request,'getsession.html',{'name':name,'lname':lname})

def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush() #to delete all the sesssion data
    return render (request,'delsession.html')