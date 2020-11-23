from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
# Create your views here.

def homepage(request):
    return render(request, 'home.html')

def filterhotel(request):
    qs = Hotel.objects.all()
    hotelname_query = request.GET.get('hotelname')
    cityname_query = request.GET.get('cityname')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')

    if hotelname_query != '' and hotelname_query is not None: 
        qs = qs.filter(hotel_name__icontains = hotelname_query)
    if cityname_query != '' and cityname_query is not None: 
        qs = qs.filter(hotel_city__icontains = cityname_query)
    if price_min != '' and price_min is not None: 
        qs = qs.filter(hotel_price__gte= price_min)
    if price_max != '' and price_max is not None: 
        qs = qs.filter(hotel_price__lt= price_max)
    
    context = {
        'queryset': qs
    }

    return render(request, 'browsehotel.html', context)

def accountpage(request):
    if request.user.is_authenticated:
        return render(request, 'myaccount.html')
    else:
        return redirect('login')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'Username OR Password is incorrect.')
            

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    messages.success(request, 'You have successfully signed out.')
    return redirect('login')

def signupPage(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                name = form.cleaned_data.get('first_name')
                messages.success(request, 'Your account has been created, ' +  name)

                return redirect('login')

    context = {'form':form}
    return render(request, 'signup.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
    
        if form.is_valid():
            form.save()
            messages.success(request, 'Your changes were saved.')
            return redirect('myaccount')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request, 'editprofile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully changed.')
            return redirect('myaccount')
        else:
            messages.warning(request, 'Invalid Data provided. Please try again.')
            return redirect('editpassword')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form':form}
        return render(request, 'editpassword.html', args)