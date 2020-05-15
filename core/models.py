from django.db import models
from django.conf import settings

# Create your models here.


CATEGORY_CHIOCES = (
    ('S', 'Shirt'),
    ('SW', 'Sport Wear'),
    ('OW', 'Outwear'),


)


LABEL_CHIOCES = (
    ('pri', 'primary'),
    ('sec', 'secondary'),
    ('inf', 'info'),
    ('dan', 'danger'),
    ('dar', 'dark'),
    ('suc', 'successs'),
    ('war', 'warning'),


)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHIOCES, max_length=2)
    label = models.CharField(choices=LABEL_CHIOCES, max_length=3)

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.username.username
