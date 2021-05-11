from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from enums.genre import GenreEnum


class Film(models.Model):
    code = models.IntegerField(
        unique=True,
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(9999),
        ],
    )
    name = models.CharField(
        max_length=128,
        unique=True,
        null=False,
        blank=False,
    )
    genre = models.CharField(
        max_length=128,
        choices=GenreEnum.choices(),
        null=True,
    )
    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(1850),
            MaxValueValidator(2100),
        ],
    )
    producer = models.ForeignKey(
        'Celebrity',
        null=True,
        related_name='film_producer',
        on_delete=models.CASCADE,
    )
    actors = models.ManyToManyField(
        'Celebrity',
        related_name="film_actors",
    )
    length = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(360),
        ],
    )
    poster = models.ImageField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.code} | {self.name} ({self.genre}, {self.length} минут) | {self.producer} "


class Celebrity(models.Model):
    is_actor = models.BooleanField()
    is_producer = models.BooleanField()
    name = models.CharField(
        max_length=128,
        null=False,
        blank=False,
    )
    surname = models.CharField(
        max_length=128,
        null=True,
    )
    age = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(150),
        ],
    )
    works_amount = models.IntegerField(
        null=False,
        default=0,
        validators=[
            MinValueValidator(0)
        ],
    )

    def __str__(self):
        return f"{self.name} {self.surname}"
