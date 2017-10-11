# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers

# Create class here
from apps.popup_admin.models import Person
from apps.popup_card.models import Comment

class UserMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = {'id', 'first_name' 'last_name'}

class ProfileMinSerializer(serializers.ModelSerializer):
    user = UserMinSerializer(many=True)

    class Meta:
        module = Person
        fields = {'name', 'avatar', 'user'}

class CommentSerializer(serializers.ModelSerializer):
    create_date = ProfileMinSerializer(many=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'card_post', 'commend_related', 'is_reply', 'create_date', 'create_user')

# class CommentSerializerGeneric(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     content = serializers.CharField(max_length=None, min_length=1, trim_whitespace=False)
#     card_post = serializers.IntegerField(read_only=True)
#     commend_related = serializers.IntegerField(read_only=True)
#     is_reply = serializers.BooleanField()
#     create_user = serializers.ListField(
#         id_user = serializers.IntegerField(read_only=True),
#         user_name = serializers.IntegerField(required=False),
#         url_image = serializers.CharField(read_only=True)
#     )