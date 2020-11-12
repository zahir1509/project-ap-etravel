from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm

from .forms import *
# Create your views here.

def homepage(request):
    return render(request, 'home.html')

def loginPage(request):
    context = {}
    return render(request, 'login.html', context)

def signupPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request, 'signup.html', context)