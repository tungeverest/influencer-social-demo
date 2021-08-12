import os
import time
import pytz
import datetime
import itertools
import random

from django.db import models
from django.db.models.deletion import PROTECT, CASCADE, SET_NULL
from django.conf import settings
from influencer.apps.users.models import UserModel
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
from unixtimestampfield.fields import UnixTimeStampField
from influencer.apps.libs.choice_model import TIMEZONES
# Create your models here.


class Career(models.Model):
    name_local = models.CharField(max_length=100, db_index=True)
    name_en = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'careers'
        ordering = ['name_local', 'name_en']

    def __str__(self):
        return str(self.name_local)


class Category(models.Model):
    name_local = models.CharField(max_length=100, db_index=True)
    name_en = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'category'
        ordering = ['name_local', 'name_en']

    def __str__(self):
        return str(self.name_local)


class TopicTag(models.Model):
    name_local = models.CharField(max_length=100, db_index=True)
    name_en = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'topic_tags'
        ordering = ['name_local', 'name_en']

    def __str__(self):
        return str(self.name_local)


class Location(models.Model):
    zip_code = models.CharField(max_length=10, unique=True)
    name_local = models.CharField(max_length=100, db_index=True)
    name_en = models.CharField(max_length=100, db_index=True)
    country = CountryField(default='VN', blank_label="Select country")

    class Meta:
        db_table = 'location'
        ordering = ['-id']

    def __str__(self):
        return str(self.name_local)

class Social(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'social'
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Influencers(models.Model):
    # refer = models.ForeignKey(
    #     UserModel, on_delete=SET_NULL, null=True, blank=True,
    #     related_name="user"
    # )
    influencer_code = models.CharField(max_length=10, unique=True)
    name = models.CharField(
        max_length=30, blank=True, null=True, db_index=True
    )
    country = CountryField(default='VN', blank_label="Select country")

    rating = models.FloatField(default=0)
    reach = models.FloatField(default=0)
    relevance = models.FloatField(default=0)
    resonance = models.FloatField(default=0)
    description = models.CharField(max_length=2000, blank=True, null=True)

    careers = models.ManyToManyField(
        Career,through="InfluencerCareers", related_name="careers",
    )
    categories = models.ManyToManyField(
        Category,through="InfluencerCategory", related_name="categories",
    )
    topic_tags = models.ManyToManyField(
        TopicTag,through="InfluencerTopicTag", related_name="topic_tags",
    )
    locations = models.ManyToManyField(
        Location,through="InfluencerLocation", related_name="locations",
    )
    socials = models.ManyToManyField(
        Social,through="InfluencerSocial", related_name="socials",
    )

    class Meta:
        db_table = 'influencers'
        ordering = ['-id']
        permissions = (
            ("view_influencer", "Can view influencers"),
        )

    @staticmethod
    def genrate_influencer_code(number):
        lower = 10**(number-1)
        upper = 10**number - 1
        random_randint = random.randint(lower, upper)
        while Influencers.objects.filter(influencer_code = random_randint).exists():
            random_randint = Influencers.genrate_influencer_code(number)

        return random_randint

    def save(self, **kwargs):
        self.pin_code = str(Influencers.genrate_influencer_code(10))
        return super().save(**kwargs)

    def __str__(self):
        return str(self.influencer_code)



class InfluencerCareers(models.Model):
    influencer = models.ForeignKey(
        Influencers, on_delete=CASCADE
    )
    career = models.ForeignKey(
        Career, on_delete=CASCADE, related_name="career"
    )

    class Meta:
        db_table = 'influencer_careers'


class InfluencerCategory(models.Model):
    influencer = models.ForeignKey(
        Influencers, on_delete=CASCADE
    )
    category = models.ForeignKey(
        Category, on_delete=CASCADE, related_name="category"
    )

    class Meta:
        db_table = 'influencer_category'


class InfluencerTopicTag(models.Model):
    influencer = models.ForeignKey(
        Influencers, on_delete=CASCADE
    )
    topic_tag = models.ForeignKey(
        TopicTag, on_delete=CASCADE, related_name="topic_tag"
    )

    class Meta:
        db_table = 'influencer_topic_tag'


class InfluencerSocial(models.Model):
    influencer = models.ForeignKey(
        Influencers, on_delete=CASCADE
    )
    social = models.ForeignKey(
        Social, on_delete=CASCADE, related_name="social"
    )
    link = models.CharField(max_length=255, unique=True)
    currency = models.CharField(max_length=3)
    price = models.IntegerField(default=0)
    fans_quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'influencer_social'


class InfluencerLocation(models.Model):
    influencer = models.ForeignKey(
        Influencers, on_delete=CASCADE
    )
    location = models.ForeignKey(
        Location, on_delete=CASCADE, related_name="location"
    )

    class Meta:
        db_table = 'influencer_location'

