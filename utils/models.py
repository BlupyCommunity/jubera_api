from django.db import models
from django.utils.datetime_safe import datetime


def auto_number(queryset, prefix='PRD', length=10):

    count = queryset.count() + 1

    if length == 10:
        return "{}-{:0>10}".format(prefix.upper(), count )

    if length == 15:
        return "{}-{:0>15}".format(prefix.upper(), count )

    if length == 20:
        return "{}-{:0>20}".format(prefix.upper(), count )


class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
