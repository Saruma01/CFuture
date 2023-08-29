#маршрутизатор - по запросу пользователядает задачу views.py
from django.contrib import admin
from django.urls import path
from .views import index, top_sellers, advert_post
from app_auth.views import logout_view
 
#хранит ссылки, а path() - создает ссылку и указывает views
urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers', top_sellers, name='top-sellers'),
    path('advertisement-post', advert_post, name='advertisement-post'),
    path('logout/', logout_view, name='logout')
]
