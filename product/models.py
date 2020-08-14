from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    SIZE_CHOICE = (
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
    )
    COLOR_CHOICE = (
        ('red', 'Red'),
        ('white', 'White'),
        ('black', 'Black')
    )
    name = models.CharField(max_length=150)
    new_price = models.DecimalField(max_digits=8, decimal_places=2)
    old_price = models.DecimalField(max_digits=8, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    description = models.TextField()
    size = models.CharField(max_length=5, choices=SIZE_CHOICE)
    color = models.CharField(max_length=5, choices=COLOR_CHOICE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    sell_count = models.IntegerField(default=0)
    featured_image = models.ImageField(upload_to='featured_image', blank=True, null=True)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='gallery')

    def __str__(self):
        return str(self.pk)



