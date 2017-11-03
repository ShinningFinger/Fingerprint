# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=255)
    UID = models.IntegerField()
    FPList = models.TextField(default='')
    OS = models.CharField(max_length=20,default='')
    Browser = models.CharField(max_length=32,default='')
