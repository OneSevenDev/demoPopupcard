# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from business.base.Enums import EnumCategory
from business.base.models import Type_general, Tag_general, BaseEntity, Status_general


# Create your models here.
class Category_card(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=500, unique=True)
    status = models.ForeignKey(Status_general)

    def __str__(self):
        return self.name

class Status_price(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Popup_card(BaseEntity, models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=500, unique=True)
    description = models.TextField(blank=True)
    type = models.ForeignKey(Type_general, null=True, blank=True)
    tag = models.ManyToManyField(Tag_general)
    category = models.ForeignKey(Category_card, null=True, blank=True)
    image = models.ImageField(upload_to='card-popup', blank=True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('create_date',)

class Popup_card_catalog(BaseEntity, models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=500,unique=True)
    type = models.ForeignKey(Type_general, null=True, blank=True)
    tag = models.ManyToManyField(Tag_general)
    card = models.ManyToManyField(Popup_card)

    def __str__(self):
        return self.name

class Price_popup_card(models.Model):
    description = models.CharField(max_length=200, null=True)
    start_date = models.DateTimeField('Init Price')
    end_date = models.DateTimeField('Finish Price')
    status = models.ForeignKey(Status_price)
    price = models.DecimalField(max_digits=21,decimal_places=5)
    percentage_discount = models.SmallIntegerField(null=True)
    quantity_discount = models.DecimalField(max_digits=18, decimal_places=2)

class Comment(BaseEntity, models.Model):
    content = models.TextField()
    card_post = models.ForeignKey(Popup_card)
    commend_related = models.BigIntegerField(null=True, blank=True)
    is_reply = models.BooleanField(default=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ('create_date',)

class Like(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    card_post = models.ForeignKey(Popup_card)
    user_click = models.ForeignKey(User)
    is_like = models.BooleanField(default=True)