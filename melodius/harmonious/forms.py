from __future__ import unicode_literals

from django.db import models
from .models import Song
from django.forms import ModelForm, Form, BaseFormSet, BaseModelFormSet
from  django import forms

from django.contrib.auth.models import User


# Create your forms here.

class SongForm(ModelForm):
    prefix = 'song'

    class Meta:
        model = Song
        exclude = ('album',)