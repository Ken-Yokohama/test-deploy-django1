from django.contrib import admin
from api.models import Blog, Author, Post

# Register your models here.
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Post)