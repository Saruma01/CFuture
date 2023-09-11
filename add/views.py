from django.db.models import Count
from django.shortcuts import render, redirect
from .models import Advert
from .forms import AdvertForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User=get_user_model()

def index(request):
    title= request.GET.get('query')
    if title:
        adverts= Advert.objects.filter(title__iregex=title)
    else:
        adverts= Advert.objects.all()
    context = {'adverts': adverts, 'title': title}
    return render(request, 'add/index.html', context)

def top_sellers(request):
    users = User.objects.annotate(adv_count=Count('advert')).order_by('-adv_count')
    context = {'users':users}
    return render(request, 'add/top-sellers.html', context)

@login_required(login_url=reverse_lazy('login'))
def advert_post(request):
    if request.method =='POST':
       form= AdvertForm(request.POST, request.FILES)
       if form.is_valid():
           advertisement=Advert(**form.cleaned_data)
           advertisement.user= request.user
           advertisement.save()
           url=reverse('main-page')
           return redirect(url)
    else:
        form = AdvertForm()
        context = {'form':form}
        return render(request,'add/advertisement-post.html', context)
    

def advert_detail(request,pk):
    advert = Advert.objects.get(id=pk)
    context = {'advert': advert,}
    return render(request, 'add/advertisement.html', context)