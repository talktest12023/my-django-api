from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)  # A short title (text)
    content = models.TextField()  # The main blog content (long text)
    date_posted = models.DateTimeField(
        auto_now_add=True)  # Auto adds date when created
    author = models.CharField(
        max_length=100, default="Anonymous")  # New field added!


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)  # New field added

    def __str__(self):
        return self.title  # Show title in the admin panel
