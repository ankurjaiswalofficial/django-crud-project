from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(verbose_name="Price", max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(verbose_name="Category", to=Category, related_name='products',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.name
