from django.shortcuts import render, redirect

from films.models import Film
from users.models import UserProfile
from ratings.models import Review, AverageRating


def my_ratings(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('login')
        return render(request, 'catalog/my_ratings.html', {
            'is_admin': request.user.is_staff,
            'account': request.user,
            'ratings': Review.objects.filter(user=request.user)
        })


def rate(request, pk):
    if request.method == "GET":
        return render(request, 'catalog/rate.html', {
            'is_admin': request.user.is_staff,
            'profile': UserProfile.objects.get(user=request.user),
            'account': request.user,
            'film': Film.objects.get(id=pk)
        })
    if request.method == "POST":
        get_rating = request.POST.get('rating')
        get_review = request.POST.get('review')
        review = Review.objects.create(
            film_id=pk,
            user=request.user,
            text_review=get_review,
            rating=get_rating
        )
        review.save()
        film = Film.objects.get(id=pk)
        avg = AverageRating.objects.get(film=film)
        avg.reviews.add(review)
        avg.average_rating = round(sum([review.rating for review in avg.reviews.all()]) / float(avg.reviews.count()), 2)
        avg.save()
        return redirect('film', pk)
