from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class BookShop(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=60)
    description = models.TextField()
    price = models.CharField(max_length=10)
    genre = models.CharField(max_length=10)
    author = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    date = models.DateField(date_added=True)