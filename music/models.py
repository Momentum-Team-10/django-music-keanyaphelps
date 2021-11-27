from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=200, blank=False)
    artist = models.CharField(max_length=200, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Create your models here.
#create a class called Album(name of model)-custom class
#field #1 is title,  CharField(max_length=200, blank=False)
#field #2 is artist, CharField(max_length=200, blank=False)
#field #3 is created_at  DateTimeField(auto_now_add=True)
