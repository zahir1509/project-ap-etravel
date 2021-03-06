from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .forms import *
from .models import *
# Create your views here.

def homepage(request):
    return render(request, 'home.html')

def filterhotel(request): #Browse Hotels
    qs = Hotel.objects.all()
    hotelname_query = request.GET.get('hotelname') #filter by name
    cityname_query = request.GET.get('cityname') #city
    price_min = request.GET.get('price_min') #min price
    price_max = request.GET.get('price_max') #max price

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

def hotelpage(request, hotel_id): #hotel details page
    hotel = get_object_or_404(Hotel, pk=hotel_id) #get hotel by id as primary key
    reviews = Review.objects.filter(hotel=hotel) #get reviews to display
    reviews_avg = reviews.aggregate(Average_Rating = Avg('rate')) #get avg of ratings
    reviews_count = reviews.count() #number of reviews/ratings

    
    if request.method == 'POST': #review/rating form
        rate_form = Rateform(request.POST)
        user = request.user

        if rate_form.is_valid():
            rate = rate_form.save(commit=False)
            rate.user = user
            rate.hotel = hotel

            rate_form.save()
            return redirect('hotelpage', hotel_id)

    else:
            rate_form = Rateform()

    context = {
        'hotel':hotel,
        'reviews':reviews,
        'reviews_avg':reviews_avg,
        'reviews_count':reviews_count,
        'rate_form':rate_form
    }
    return render(request, 'hotel.html', context)



def bookhotel(request): #hotel booking form on hotel detail page
    if request.method == "POST":
        hotel_id = request.POST.get('hotel', '')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        num_people = request.POST.get('num_people')
        rooms = request.POST.get('rooms')

    hotel = get_object_or_404(Hotel, pk = hotel_id)

    #create an instance of reservation class for the user
    booknow = Reservation (
        user = request.user,
        reservation_name = hotel.hotel_name + " | " + request.user.username,
        reference_name = hotel.hotel_name + ", " + hotel.hotel_city,
        check_in = check_in,
        check_out = check_out,
        num_people = num_people,
        rooms = rooms,
        cost = hotel.hotel_price * float(rooms),
        timestamp = datetime.now()
    )
    booknow.save()

    return render(request, 'bookingpage.html', {'hotel':hotel, 'booking':booknow})

def cancelbooking(request): #cancel booking
    if request.method == 'POST':
        reservation_id = request.POST.get('reservation', '')
    #get reservation by id as primary key
    reservation = get_object_or_404(Reservation, pk = reservation_id)

    booked = Reservation.objects.filter(
        user = request.user,
        pk = reservation_id
    )
    booked.delete() #delete it
    messages.info(request, 'Your reservation was cancelled.')
    return redirect('myaccount')

def accountpage(request): #show user profile and reservations
    if request.user.is_authenticated:
        reservation_list = Reservation.objects.filter(user = request.user)
        context = {
            'user': request.user,
            'reservation_list' : reservation_list
        }
        return render(request, 'myaccount.html', context)
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
            update_session_auth_hash(request, form.user) #prevent logout after password change
            messages.success(request, 'Your password was successfully changed.')
            return redirect('myaccount')
        else:
            messages.warning(request, 'Invalid Data provided. Please try again.')
            return redirect('editpassword')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form':form}
        return render(request, 'editpassword.html', args)

