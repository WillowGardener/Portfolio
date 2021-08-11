from django.db import models


class Category(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    price = models.FloatField()
    category_set = models.ManyToManyField(Category, related_name='product_set', blank=True)
    main_image = models.ImageField(default='images/no_image_available.png')

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    image = models.ImageField(upload_to='images',blank=True)
    alt_text = models.CharField(max_length=100, blank=True)
    product = models.ManyToManyField(Product, blank=True, related_name='product_images')

    def __str__(self):
        return self.alt_text
