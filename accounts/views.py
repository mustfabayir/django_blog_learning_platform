from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

def login_request(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/login.html', {"error": "Username or Password is incorrect!"})

    return render(request, 'account/login.html')

def register_request(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, 'account/register.html', {'error': 'Username has already been use!'})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'account/register.html', {'error': 'Email has already been use!'})
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect('login')
        else:
            return render(request, 'account/register.html', {'error': 'Password did not match!'})

    return render(request, 'account/register.html')

def logout_request(request):
    logout(request)

    return redirect('home')

