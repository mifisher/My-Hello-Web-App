from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Thing (models.Model):
    name = models.CharField (max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, blank=True, null=True)
