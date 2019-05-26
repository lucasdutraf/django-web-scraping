from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True, blank=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    price = models.CharField(max_length=50, blank=False, null=False)
    image_link = models.URLField(max_length=150)

    def __str__(self):
        return self.name