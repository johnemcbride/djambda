import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Instrument(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Band(models.Model):

    name = models.CharField(max_length=200)
    instruments = models.ManyToManyField(Instrument, blank=True)

    def __str__(self):
        return self.name


class BandPackage(models.Model):
    name = models.CharField(max_length=200)
    full_price = models.FloatField(default=0)
    under_30s_price = models.FloatField(default=0)
    sibling_price = models.FloatField(default=0)
    bands = models.ManyToManyField(Band, blank=True)

    def __str__(self):
        return self.name
