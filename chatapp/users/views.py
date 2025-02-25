from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def Signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "your passwords is not matched")
        elif User.objects.filter(username = username).exists():
            messages.error(request, "user name is already exist")
        elif User.objects.filter(email = email).exists():
            messages.error(request, "user Email is already exist")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            messages.success(request,"User signup successfully")
            return redirect('home')
    return render(request, 'signup.html')

@login_required(login_url='login')
def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "login successfully")
            return redirect('home')
        else:
            messages.error(request, 'username and password is incorrect')
    return render(request, 'signin.html')

def logout_view(request):
    logout(request)
    messages.success(request, "logout successfully")
    return redirect('login')