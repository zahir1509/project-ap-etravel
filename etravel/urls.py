"""etravel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name = 'home'),
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('signup/', views.signupPage, name = 'signup'),
    path('browsehotel/', views.filterhotel, name = 'browsehotel'),
    path('myaccount/', views.accountpage, name='myaccount'),
    path('editprofile/', views.edit_profile, name='editprofile'),
    path('change-password/', views.change_password, name='editpassword'),
    path('hotel_booking/', views.bookhotel, name='bookhotel'),
    path('hotel/<int:hotel_id>', views.hotelpage, name='hotelpage'),
    path('cancelbooking/', views.cancelbooking, name='cancelbooking'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
