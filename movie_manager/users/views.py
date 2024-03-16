from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# Create your views here.
def login(request):
    error_message = None
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            print(user)
            auth_login(request, user)
            return redirect("list")
        else:
            error_message = "Invalid credentials"
    return render(request, "users/login.html", {"error_message": error_message})


def logout(request):
    auth_logout(request)
    return redirect("login")


def signup(request):
    user = None
    error_message = None
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.create_user(username=username, password=password)
        except Exception as e:
            error_message = str(e)
        # print(user)
    return render(
        request, "users/create.html", {"user": user, "error_message": error_message}
    )
