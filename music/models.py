from django.db import models


# Create your models here.


class Music(models.Model):
    name_music = models.CharField(
        max_length=50,
        verbose_name = 'name music'
    )
    artist = models.CharField(
        max_length=255,
        verbose_name = 'artist'
    )
    genre = models.CharField(
        max_length=255,
        verbose_name = 'genre'
    )
    link_music = models.CharField(
        max_length=255,
        verbose_name = 'link_music'
    )
