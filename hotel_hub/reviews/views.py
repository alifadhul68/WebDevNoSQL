from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Review
from hotels.models import Hotel
from datetime import datetime

# Create your views here.

def review_list(request):
    latest_review_list = Review.objects.order_by('-publish_date')[:5]
    hotels = Hotel.objects.all()
    rating_choices = Review.rating_choices
    context = {
        'myrange': range(1),
        'latest_review_list': latest_review_list,
        'hotels': hotels,
        'rating_choices': rating_choices,
    }
    return render(request, 'reviews/review_list.html', context)
    
def review_create(request):
  if request.method == 'POST':
    hotel_id = request.POST['hotel']
    user = request.POST['user']
    comment = request.POST['comment']
    rating = request.POST['rating']
    publish_date = datetime.today()

    hotel = Hotel.objects.get(id=hotel_id)

    review = Review()
    review.hotel = hotel
    review.user = user
    review.comment = comment
    review.rating = rating
    review.publish_date = publish_date

    review.save()

    return redirect(reverse('reviews:review_list'))