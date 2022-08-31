from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    #title
    title = models.CharField(max_length=128)

    #text
    text = models.TextField(blank=True)

    #author
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #created_date
    created_date = models.DateTimeField(auto_now=True)

    #modified_date
    modified_date = models.DateField(auto_now=True)

    #published_date
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title

