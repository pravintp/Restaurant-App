from django.db.models import Count, Avg
from django.shortcuts import render, get_object_or_404

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


def restaurant_detail_view(request, pk):
    return render(
        request,
        "my_restaurant/detail.html",
        {"restaurant": get_object_or_404(Restaurant, pk=pk)},
    )
