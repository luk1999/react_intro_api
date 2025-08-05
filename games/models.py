from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL


class Platform(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Rating(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    platform = models.ForeignKey(Platform, on_delete=models.RESTRICT)
    developer = models.ForeignKey(Developer, on_delete=models.RESTRICT)
    genre = models.ForeignKey(Genre, on_delete=models.RESTRICT)
    rating = models.ForeignKey(Rating, null=True, on_delete=models.RESTRICT)
    released_at = models.DateField()
    meta_score = models.PositiveSmallIntegerField(null=True)
    user_score = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    comment = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:50]
