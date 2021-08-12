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

from influencer.apps.influencers.models import Influencers, Social
# Create your models here.


class Interest(models.Model):
    name_local = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'interest'
        ordering = ['-id']

    def __str__(self):
        return str(self.name_en)


class FanInterest(models.Model):
    interest = models.ForeignKey(
        Interest, on_delete=CASCADE, related_name="interest"
    )
    influencer = models.ForeignKey(
        Influencers, on_delete=CASCADE, related_name="fan_interest_influencer"
    )
    social = models.ForeignKey(
        Social, on_delete=CASCADE, related_name="fan_interest_social"
    )
    fans_quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'fan_interest'


class AgeRange(models.Model):
    age_range_min = models.IntegerField(default=0)
    age_range_max= models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'age_range'

    def __str__(self):
        return (str(self.age_range_min) + ' - ' + str(self.age_range_max))


class FanAgeRange(models.Model):
    age = models.ForeignKey(
        AgeRange, on_delete=CASCADE, related_name="age_range"
    )
    influencer = models.ForeignKey(
        Influencers, on_delete=CASCADE, related_name="fan_age_influencer"
    )
    social = models.ForeignKey(
        Social, on_delete=CASCADE, related_name="fan_age_social"
    )
    fans_quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'fan_age_range'
