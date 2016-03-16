from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    """
    The User object
    """
    # The User's username
    username = models.CharField(max_length=30)
    # The User's email
    email = models.EmailField()
    # The User's password final hash
    hash = models.CharField(max_length=32)
    # The User's password salt
    salt = models.CharField(max_length=32)


class Room(models.Model):
    """
    The model representing a group of students
    """
    # The Room's users who have administrative rights
    owners = models.ManyToManyField(User)
    # The Room's users who are just listening
    listeners = models.ManyToManyField(User)
    # The preferences for the Room
    preferences = models.TextField()