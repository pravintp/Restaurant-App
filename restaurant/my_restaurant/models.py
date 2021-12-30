from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Menu(models.Model):
    pass


class Location(models.Model):
    name = models.CharField(max_length=50)


class Restaurant(models.Model):
    VEGAN = "Vegan"
    VEGETARIAN = "Veg"
    NON_VEGETARIAN = "Non-veg"

    TYPE_CHOICES = [
        (VEGAN, "Vegan"),
        (VEGETARIAN, "Vegetarian"),
        (NON_VEGETARIAN, "Non-Vegetarian"),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    cost_for_two = models.CharField(max_length=4)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    door_no = models.CharField(max_length=7)
    street = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    pincode = models.CharField(max_length=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)


class Item(models.Model):
    name = models.CharField(max_length=50)
    whether_veg = models.BooleanField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)


class Photo(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="pictures/")


class Cuisine(models.Model):
    name = models.CharField(max_length=30)


class RestaurantHasCuisine(models.Model):
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class BookmarkLet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class UserVisited(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
