from django.db import models

class book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
