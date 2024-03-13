from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='imagens_products/', null=True, blank=True)
    ean = models.CharField(max_length=13, unique=True)
    price_min = models.DecimalField(max_digits=8, decimal_places=2)
    price_max = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class VariationPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    data = models.DateField()
    price_min = models.DecimalField(max_digits=8, decimal_places=2)
    price_max = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.price} - {self.data}"