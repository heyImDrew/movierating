from django.contrib import admin
from films.models import (
    Film,
    Celebrity
)

admin.site.register(Film)
admin.site.register(Celebrity)
