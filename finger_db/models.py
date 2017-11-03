# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from UserData.models import User
# Create your models here.


class myField(models.Field):
    def db_type(self, connection):
        return 'NVARCHAR(4000)'

class Request(models.Model):
#     # browser ID
    browserID = models.ForeignKey(User,null= True)
    # passive collection
    HeaderOrder = models.CharField(max_length=255)
    UserAgent_in_the_request = models.TextField(default='')
    AcceptType = models.TextField(default='')
    AcceptEncoding= models.CharField(max_length = 128)
    AcceptLanguage= models.CharField(max_length = 128)
    IPAddress=models.GenericIPAddressField()
    time = models.DateTimeField(auto_now_add=True)
    DNT= models.BooleanField(default=False)

    # active collection
    User_Agent_obtained_by_JS = models.TextField(default='')
    OS = models.CharField(max_length=20,default='')
    OS_Version = models.CharField(max_length=32,default='')
    Browser = models.CharField(max_length=32,default='')
    BrowserVersion = models.CharField(max_length=50,default='')
    ScreenResolution = models.CharField(max_length=50,default='')
    AvailableViewArea = models.CharField(max_length=50,default='')
    ZoomRatio = models.FloatField(default=0.0)
    AspectRation = models.FloatField(default=0.0)
    Plugins = myField()
    Font = myField()
    TimeZone = models.CharField(max_length=16,default='')

    FlashEnabled = models.BooleanField(default=False)
    CookiesEnabled = models.BooleanField(default=False)

    Flash_Version = models.CharField(max_length=32,default='')
    Color_Depth = models.IntegerField(default=0)
    Language = models.CharField(max_length=128,default='')
    Canvas = models.TextField(default='')
    AdBlock = models.BooleanField(default=False)
    isJava = models.BooleanField(default=False)
    isLocalStorage = models.BooleanField(default=False)
    isSessionStorage = models.BooleanField(default=False)
    FingerPrint = models.BigIntegerField(default=0)
    count = models.IntegerField(default=0)

class key(models.Model):
    column_name = models.CharField(max_length=100,default='')



