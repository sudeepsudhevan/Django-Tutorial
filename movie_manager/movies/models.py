from django.db import models

# Create your models here.


class CensorInfo(models.Model):
    rating = models.CharField(max_length=10, null=True)
    certified_by = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.certified_by


class Director(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MovieInfo(models.Model):  # inherits from models.Model
    title = models.CharField(max_length=200)
    year = models.IntegerField(null=True)
    summary = models.TextField(max_length=1000, blank=True)
    poster = models.ImageField(upload_to="images/", null=True)
    censor_details = models.OneToOneField(
        CensorInfo, on_delete=models.SET_NULL, related_name="movie", null=True
    )
    directed_by = models.ForeignKey(
        Director, on_delete=models.CASCADE, related_name="directed_movies", null=True
    )
    actors = models.ManyToManyField(Actor, related_name="acted_movies")

    def __str__(self):
        return self.title
