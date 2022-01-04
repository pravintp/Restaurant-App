from django.contrib import admin

from .models import (
    Restaurant,
    Item,
    Review,
    Photo,
    Cuisine,
    Menu,
    RestaurantHasCuisine,
    BookmarkLet,
    UserVisited,
)

# Register your models here.


admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Review)
admin.site.register(Photo)
admin.site.register(Cuisine)
admin.site.register(Menu)
admin.site.register(RestaurantHasCuisine)
admin.site.register(BookmarkLet)
admin.site.register(UserVisited)
