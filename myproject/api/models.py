from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    blog_desc = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body_text = models.TextField()
    date_created = models.DateField()
    rating = models.IntegerField()
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title