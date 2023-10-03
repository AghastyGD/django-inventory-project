from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('Electrônicos', 'Eletrônicos'),
    ('Comida', 'Comida'),
    ('Livros', 'Livros'),
    ('Imovéis', 'Imovéis'),
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Produto'

    def __str__(self):
        return f'{self.name}: {self.quantity}'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'

