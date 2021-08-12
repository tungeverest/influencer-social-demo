import os
import pytz
import time
import datetime
import itertools
import random, string

from django.db import models
from django.db.models.deletion import PROTECT, CASCADE, SET_NULL
from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import IntegrityError, models, transaction
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model

from influencer.apps.influencers.models import Influencers, TopicTag, Social
from influencer.apps.libs.choice_model import (
    ACTION_TYPES,POST_TYPES, TIMEZONES
)
# Create your models here.


class Hashtag(models.Model):
    name_local = models.CharField(max_length=100, db_index=True)
    name_en = models.CharField(max_length=100, db_index=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'hash_tag'
        ordering = ['-id']

    def __str__(self):
        return str(self.name_en)


class Post(models.Model):
    post_code = models.CharField(max_length=16, unique=True)
    influencer = models.ForeignKey(
        Influencers, on_delete=PROTECT, related_name="influencer"
    )
    social = models.ForeignKey(
        Social, on_delete=PROTECT, related_name="post_social"
    )
    topic_tag = models.ForeignKey(
        TopicTag, on_delete=SET_NULL, null=True, blank=True,
        related_name="post_topic_tag"
    )
    hash_tag = models.ManyToManyField(
        Hashtag, through="PostHashTag", related_name="hash_tag",
    )
    post_type = models.CharField(
        max_length=30, choices=POST_TYPES,  null=True, blank=True,
    )
    link = models.TextField(max_length=500)
    rating = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)

    #random PIN
    @staticmethod
    def genrate_post_code(number):
        lower = 10**(number-1)
        upper = 10**number - 1
        random_randint = random.randint(lower, upper)
        while Post.objects.filter(post_code = random_randint).exists():
            random_randint = Post.genrate_post_code(number)

        return random_randint

    def save(self, **kwargs):
        self.post_code = str(Post.genrate_post_code(16))
        return super().save(**kwargs)

    class Meta:
        db_table = 'posts'
        ordering = ['-id']

    def __str__(self):
        return str(self.post_code)


class PostHashTag(models.Model):
    post = models.ForeignKey(
        Post, on_delete=CASCADE, related_name="tag_posts"
    )
    hash_tags = models.ForeignKey(
        Hashtag, on_delete=CASCADE, related_name="hash_tags"
    )

    class Meta:
        db_table = 'post_hash_tag'


class PostAction(models.Model):
    post = models.ForeignKey(
        Post, on_delete=CASCADE,
        related_name="posts", db_index=True
    )
    type_action = models.CharField(
        max_length=30, choices=ACTION_TYPES
    )
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'post_action'
        ordering = ['-id']

    def __str__(self):
        return str(self.type_action)
