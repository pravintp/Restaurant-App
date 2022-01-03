from django.db.models import Count, Avg
from django.shortcuts import render

from .models import Restaurant, Photo

# Create your views here.


def restaurant_list_view(request):
    return render(
        request,
        "my_restaurant/list.html",
        {
            "restaurants": Restaurant.objects.annotate(
                nreviews=Count("reviews"), avg=Avg("reviews__rating")
            )
        },
    )
