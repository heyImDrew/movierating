from django.contrib import admin
from ratings.models import Review, AverageRating

admin.site.register(Review)
admin.site.register(AverageRating)
