from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=254)
    description_short = models.TextField()
    description_long = models.TextField()
    product_nr = models.CharField(unique=True, max_length=254)
    count = models.IntegerField()
    weight = models.FloatField()
    product_img = models.ImageField()
