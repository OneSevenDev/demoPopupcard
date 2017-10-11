# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Status_general(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Type_general(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Tag_general(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class BaseEntity(models.Model):
    priority_order = models.IntegerField(default=100)
    create_date = models.DateTimeField('Create date', auto_now_add=True)
    create_user = models.ForeignKey(User,related_name='create_user')
    update_date = models.DateTimeField('Update date', auto_now=True)
    update_user = models.ForeignKey(User, null=True, related_name='update_user', blank=True)
    status = models.ForeignKey(Status_general, null=True, blank=True)

class MenuSetting(BaseEntity, models.Model):
    title = models.CharField(max_length=200)
    parent_id = models.PositiveIntegerField(null=True,blank=True)
    url = models.CharField(max_length=2000)
    position = models.SmallIntegerField(null=True,default=0)