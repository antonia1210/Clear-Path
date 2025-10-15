from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,  logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'USER':
                return redirect('user')
            elif user.role == 'ACCOUNTANT':
                return redirect('accountant')
            elif user.role == 'ADMIN':
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')

def home_view(request):
    return render(request, 'accounts/home_page.html')

def logout_view(request):
    logout(request)
    return redirect('login')