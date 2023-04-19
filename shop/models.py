from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.title


class product(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    product_image = models.ImageField(blank=True)
    descreption = models.TextField(max_length=190)
    quantity = models.IntegerField(blank=False, null=False)
    trending = models.BooleanField(default=False, help_text="0-default, 1-trending")
    price = models.FloatField(null=False, blank=False)
    tag = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True,null=False)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)

class wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)