from django.shortcuts import render
from .models import Advert
# Create your views here.

def index(request):
    adverts= Advert.objects.all()
    context = {'adverts': adverts}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

