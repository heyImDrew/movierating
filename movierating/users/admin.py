from django.contrib import admin
from users.models import UserProfile
from django.contrib.auth.models import Group

# Removing Groups (bc they are unnecessary)
admin.site.unregister(Group)

# Adding created models
admin.site.register(UserProfile)
