from django.shortcuts import render, redirect
from django.db.models import Prefetch
from django.urls import reverse
from .models import Hotel
from reviews.models import Review
from .forms import HotelForm

def hotel_list(request):
    hotels = Hotel.objects.all()
    reviews = Review.objects.prefetch_related('hotel')
    hotels_dict = {}
    for hotel in hotels:
        hotels_dict[hotel] = reviews.filter(hotel=hotel)
    
    context = {'hotels_dict': hotels_dict}
    return render(request, 'reviews/hotel_list.html', context)

def add(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hotels:hotel_list')
    else:
        form = HotelForm()
    return render(request, 'reviews/add.html', {'form': form})