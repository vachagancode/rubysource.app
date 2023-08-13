from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app:index')
        else:
            messages.error(request, "There was an error while logging in, Try again :(")
            return redirect('users:login')
    else:
        return render(request, "auth/login.html")
def logout_user(request):
    logout(request)
    return redirect('app:index')

def registration_user(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('app:index')
    context ={
        'form': form
    }

    return render(request, "auth/registration.html", context)