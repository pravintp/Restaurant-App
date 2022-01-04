from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


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
    door_no = models.CharField(max_length=7)
    street = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.OneToOneField(
        Restaurant, on_delete=models.CASCADE, related_name="menus"
    )

    def __str__(self):
        return self.restaurant.name


class Item(models.Model):
    VEGETARIAN = "Veg"
    NON_VEGETARIAN = "Non-veg"

    FOOD_TYPE_CHOICES = [
        (VEGETARIAN, "Vegetarian"),
        (NON_VEGETARIAN, "Non-Vegetarian"),
    ]
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=7, choices=FOOD_TYPE_CHOICES)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Photo(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="photos"
    )
    photo = models.ImageField(upload_to="pictures/")

    def __str__(self):
        return self.restaurant.name


class Cuisine(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


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
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="reviews"
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
