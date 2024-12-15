from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    has_analysis = models.BooleanField(default=False)
    url = models.URLField(max_length=200, null=True, blank=True)
    change = models.IntegerField(choices=[(-2, "-2"), (-1, "-1"), (0, "0"), (1, "1"), (2, "2")], default=0)
    categories = models.ManyToManyField(Category, related_name="products")
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
