from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)
    is_watched = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(default=None, blank=True)

    def __str__(self):
        return self.name
