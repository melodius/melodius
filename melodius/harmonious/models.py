from __future__ import unicode_literals

from django.db import models


class Song(models.Model):
    """
    The Song Object
    """
    # The Song title
    title = models.CharField(max_length=60)
    # The Song's artist
    artist = models.CharField(max_length=60,
                              null=True)
    # The Album the Song belongs to
    album = models.ForeignKey('Album',
                              null=True)


class Album(models.Model):
    """
    The Album Object
    """
    # The name of the Album
    name = models.CharField(max_length=60,
                            null=True)
    # The URL of the artwork that corresponds to the Album
    artwork_url = models.TextField(null=True)
    # The year the Album was released
    year = models.IntegerField(null=True)
    # The genre of music the Album belongs to
    genre = models.CharField(max_length=60,
                             null=True)

