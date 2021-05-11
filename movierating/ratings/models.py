from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from films.models import Film


class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
    )
    rating = models.FloatField(
        default=0,
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
    )
    text_review = models.TextField(
        max_length=1024,
        null=False,
        blank=True
    )


class AverageRating(models.Model):
    film = models.OneToOneField(
        Film,
        on_delete=models.CASCADE,
    )
    reviews = models.ManyToManyField(
        'Review',
        related_name='film_reviews',
        blank=True,
    )
    average_rating = models.FloatField(
        default=0,
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
    )


def film_created(sender, instance, created, **kwargs):
    if not AverageRating.objects.filter(film_id=instance.id):
        avg = AverageRating.objects.create(
            film_id=instance.id,
            average_rating=0
        )
        avg.save()


signals.post_save.connect(film_created, sender=Film)
