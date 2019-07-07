from django.db import models
from django.utils.datetime_safe import datetime


def auto_number(number, length=10, prefix='PRD'):
    if length == 10:
        return "{}{:0>10}".format(number, prefix.upper())

    if length == 15:
        return "{}{:0>15}".format(number, prefix.upper())

    if length == 20:
        return "{}{:0>20}".format(number, prefix.upper())


class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
