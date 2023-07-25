#маршрутизатор - по запросу пользователядает задачу views.py
from django.contrib import admin
from django.urls import path
from .views import index
#хранит ссылки, а path() - создает ссылку и указывает views
urlpatterns = [
    path('home/', index)
]
