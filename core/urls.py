from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import item_list

app_name = 'core'
urlpatterns = [
    path('', item_list, name='item_list')
]
