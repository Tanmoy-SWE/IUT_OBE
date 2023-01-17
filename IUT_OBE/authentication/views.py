from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout


# Create your views here.


def home(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password = password)
            if (user is not None):
                login(request, user)
                
            else:
                messages.info(request, "Username or Password is incorrect.")
    context = {}    
    if request.user.is_authenticated == True:
        return render(request, "homepage.html", context)        
    
    return render(request, 'Home.html', context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        username = request.POST.get('username')
        if form.is_valid():
            form.save()
            uobj = User.objects.get(username=username)    
            uobj.save()
            return redirect('LoginPage')
    context = {'form': form }
    return render(request, "register.html", context)

def logout_user(request):
    logout(request)
    return redirect('/')