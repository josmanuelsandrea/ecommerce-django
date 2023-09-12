from django.db import models
from django.db.models import SET_DEFAULT, CASCADE
from categories.models import Category
from users.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    product_image = models.ImageField(upload_to='products/imgs/')
    existence = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=SET_DEFAULT, default=1, null=False)
    seller = models.ForeignKey(User, on_delete=CASCADE, null=False)

    def __str__(self):
        return self.name