from django.contrib import admin
from .models import Destinations, Review, User

# Register your models here.

admin.site.register(Destinations)
admin.site.register(Review)
admin.site.register(User)
