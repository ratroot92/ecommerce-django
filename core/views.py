from django.shortcuts import render
from .models import Item, Order, OrderItem
# Create your views here.


def item_list(request):
    items = Item.objects.all()
    return render(request, 'home-page.html', {'items': items})
