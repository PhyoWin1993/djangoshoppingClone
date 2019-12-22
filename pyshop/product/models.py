from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=225)
    price = models.IntegerField()
    dis = models.TextField()
    image = models.ImageField(default="default.png",upload_to="product_pics")
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
