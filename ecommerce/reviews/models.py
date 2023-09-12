from django.db import models
from django.db.models import CASCADE
from users.models import User
from products.models import Product

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=CASCADE, null=False)
    comment = models.CharField(max_length=650)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f'[{self.user.username}]: {self.comment[0:21]}'