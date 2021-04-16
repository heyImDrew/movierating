from django.contrib import admin
from films.models import (
    Film,
    Series
)

admin.site.register(Series)
admin.site.register(Film)
