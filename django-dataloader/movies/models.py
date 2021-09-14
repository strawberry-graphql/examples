from django.db import models


class Director(models.Model):
    name = models.TextField()


class Movie(models.Model):
    imdb_id = models.CharField(max_length=20)
    title = models.TextField()
    year = models.IntegerField()
    image_url = models.TextField()
    imdb_rating = models.FloatField()
    imdb_rating_count = models.TextField()

    director = models.ForeignKey(Director, on_delete=models.CASCADE)
