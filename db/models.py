from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Actor(models.Model):
    first_mame = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
