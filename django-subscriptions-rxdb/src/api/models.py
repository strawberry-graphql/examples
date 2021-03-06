# -*- coding: utf-8 -*-

from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q


class Hero(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    color = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    updatedAt = models.FloatField(max_length=100, null=True)
    deleted = models.BooleanField()
