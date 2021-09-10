# -*- coding: utf-8 -*-

from django.db import models


class Hero(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    color = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    updatedAt = models.FloatField(max_length=100, null=True)
    deleted = models.BooleanField()
