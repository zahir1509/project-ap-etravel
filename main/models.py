from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.city


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=20)

    #Not sure how to use ForeignKey here
    hotel_city = models.CharField(max_length=20, default="") 
    #hotel_city = models.ForeignKey(Location, on_delete=models.CASCADE)

    hotel_address = models.CharField(max_length=40, default="")
    hotel_price = models.IntegerField()

    #hotel_img = models.ImageField()

    hotel_star = models.IntegerField()

    hotel_restaurant = models.BooleanField(default=False)
    hotel_ac = models.BooleanField(default=True)
    hotel_pool = models.BooleanField(default=False)
    hotel_spa = models.BooleanField(default=False)
    hotel_giftshop = models.BooleanField(default=False)
    hotel_wifi = models.BooleanField(default=True)
    hotel_parking = models.BooleanField(default=False)
    
    def __str__(self):
        return self.hotel_name

class HotelRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(null=True)

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    reservation_name = models.CharField(max_length=40, default="")
    timestamp = models.DateTimeField(default=datetime.now())
    num_people = models.IntegerField(default=1)
    rooms = models.IntegerField(default=1)
    check_in = models.DateField(null=True)
    check_out = models.DateField(null=True)


    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.reservation_name



