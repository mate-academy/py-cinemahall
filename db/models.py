from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=63)


class Actor(models.Model):
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
