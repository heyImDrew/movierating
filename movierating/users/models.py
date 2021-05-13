import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from enums.status import StatusEnum
from django.db.models import signals
from django.shortcuts import get_object_or_404


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='user_profile',
        on_delete=models.CASCADE,
    )
    email = models.CharField(
        max_length=255,
        null=False,
        blank=True,
    )
    account_status = models.CharField(
        null=False,
        blank=False,
        choices=StatusEnum.choices(),
        max_length=255,
    )


def user_created(sender, instance, created, **kwargs):
    if not UserProfile.objects.filter(user=User.objects.get(username=instance.username)):
        user_profile = UserProfile.objects.create(
            user=get_object_or_404(User, username=instance.username),
        )
        user_profile.account_status = StatusEnum.ENABLED.name
        user_profile.save()


signals.post_save.connect(user_created, sender=User)
