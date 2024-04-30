
from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm,EditUserChangeForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,UserChangeForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
# Create your views here.


def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                messages.success(request, 'Account created successfully')
                fm.save()
        else:
            fm = SignUpForm()
        return render(request, 'signup.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')

# login


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'userlogin.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = EditUserChangeForm(request.POST,instance =request.user)
            if fm.is_valid():
                messages.success(request,'Profile Updated')
                fm.save()
        else:
            fm = EditUserChangeForm(instance = request.user)
        return render(request, 'profile.html', {'name': request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user = request.user)
        return render(request, 'changepass.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')
