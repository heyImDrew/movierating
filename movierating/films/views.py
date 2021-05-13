from django.shortcuts import render, redirect

from films.models import Film
from enums.genre import GenreEnum
from ratings.models import AverageRating, Review


def catalog(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('login')
        return render(request, 'catalog/catalog.html', {
            'is_admin': request.user.is_staff,
            'films': list_to_raw_lists(Film.objects.all()),
            'raws': Film.objects.count() / 3
        })


def film(request, pk):
    if request.method == "GET":
        return render(request, 'catalog/film.html', {
            'reviews': Review.objects.filter(film_id=pk),
            'rating': AverageRating.objects.get(film=Film.objects.get(id=pk)).average_rating,
            'reviews_count': AverageRating.objects.get(film=Film.objects.get(id=pk)).reviews.count(),
            'film': Film.objects.get(id=pk),
            'genre': GenreEnum.get(Film.objects.get(id=pk).genre),
            'actors': Film.objects.get(id=pk).actors.all()
        })


def list_to_raw_lists(data):
    result = [[]]
    for raw in data:
        if len(result[len(result) - 1]) >= 3:
            result.append([])
        result[len(result) - 1].append(raw)
    return result
