import uuid
from django.db import models
from users.models import User
from products.models import Product

# Create your models here.

class Shopping_List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created_at = models.DateField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return f'{self.user} + {self.uuid}'

class Shopping_List_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    list_id = models.ForeignKey(Shopping_List, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False)