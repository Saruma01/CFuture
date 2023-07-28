#маршрутизатор - по запросу пользователядает задачу views.py
from django.contrib import admin
from django.urls import path
from .views import index, top_sellers
#хранит ссылки, а path() - создает ссылку и указывает views
urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers', top_sellers, name='top-sellers')
]
