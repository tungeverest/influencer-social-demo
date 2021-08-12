from time import time
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import empty
from rest_framework.validators import UniqueTogetherValidator
from django.conf import settings
from django.db import transaction
from django.utils.translation import ugettext as _
from .models import (
    Interest, AgeRange
)


class InterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interest
        fields = (
            "id",
            "name_local",
            "name_en",
            "is_active",
        )
        read_only_fields = (
            "id",
        )


class AgeRangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgeRange
        fields = (
            "id",
            "age_range_min",
            "age_range_max",
            "is_active",
        )
        read_only_fields = (
            "id",
        )

