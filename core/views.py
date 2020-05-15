from django.shortcuts import render
from .models import Item, Order, OrderItem
from django.views.generic import TemplateView, View, DetailView, ListView

# Create your views here.


class Home_View(ListView):
    model = Item
    template_name = "home-page.html"

    def get(self, request, *args, **kwargs):
        context = {
            'items': Item.objects.all()
        }

    return render(request, 'home-page.html', context)
