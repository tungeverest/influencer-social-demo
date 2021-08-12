from time import time
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import empty
from rest_framework.validators import UniqueTogetherValidator
from django.conf import settings
from django.db import transaction
from django.utils.translation import ugettext as _
from .models import (
    Hashtag, Post, PostAction
)


class HashtagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hashtag
        fields = (
            "id",
            "name_local",
            "name_en",
            "hash_tags",
            "is_active",
        )
        read_only_fields = (
            "id",
        )

class PostActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostAction
        fields = (
            "id",
            "post",
            "type_action",
            "quantity",
        )
        read_only_fields = (
            "id"
        )


class PostSerializer(serializers.ModelSerializer):

    post_action = PostActionSerializer(many=True, required=False)
    hash_tags = serializers.SerializerMethodField()

    def get_hash_tags(self, instance):
        return instance.hash_tag.all()

    class Meta:
        model = Post
        fields = (
            "id",
            "post_code",
            "influencer",
            "social",
            "topic_tag",
            "hash_tag",
            "post_type",
            "post_action",
            "link",
            "rating",
            "is_active",
        )
        read_only_fields = (
            "id",
            "post_code",
        )


