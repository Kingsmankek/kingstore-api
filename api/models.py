from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        
    def __str__(self):
        return f'{self.pk} - {self.name}'


class Region(models.Model):
    name = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'regions'
        
    def __str__(self):
        return f'{self.pk} - {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stockQuantity = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    categoryId = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    regionId = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name='products')
    image = models.BinaryField(null=True, blank=True)
    
    class Meta:
        db_table = 'products'
        
    def __str__(self):
        return f'{self.pk} - {self.name}'


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cart'
        
    def __str__(self):
        return f'{self.pk} - {self.product.name} ({self.quantity})'
