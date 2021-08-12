from time import time
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import empty
from rest_framework.validators import UniqueTogetherValidator
from django.conf import settings
from django.db import transaction
from django.utils.translation import ugettext as _
from .models import (
    Career, Category, TopicTag, Location, Social, Influencers,
    InfluencerCareers, InfluencerCategory, InfluencerTopicTag,
    InfluencerSocial, InfluencerLocation
)


class CareerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Career
        fields = (
            "id",
            "name_local",
            "name_en",
            "is_active",
        )
        read_only_fields = (
            "id",
        )


class InfluencerCareersSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfluencerCareers
        fields = (
            "id",
        )
        read_only_fields = (
            "id",
        )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "id",
            "name_local",
            "name_en",
            "is_active",
        )
        read_only_fields = (
            "id",
        )


class TopicTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = TopicTag
        fields = (
            "id",
            "name_local",
            "name_en",
            "description",
            "is_active",
        )
        read_only_fields = (
            "id"
        )


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = (
            "id",
            "zip_code",
            "name_en",
            "name_local",
            "country",
        )
        read_only_fields = (
            "id",
        )


class SocialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Social
        fields = (
            "id",
            "name",
            "is_active",
        )
        read_only_fields = (
            "id",
        )


class InfluencersSerializer(serializers.ModelSerializer):

    # careers = serializers.SerializerMethodField()
    # categories = serializers.SerializerMethodField()
    # topic_tags = serializers.SerializerMethodField()
    # locations = serializers.SerializerMethodField()
    # socials = serializers.SerializerMethodField()

    # def get_careers(self, instance):
    #     return instance.careers.all()
    # def get_categories(self, instance):
    #     return instance.categories.all()
    # def get_topic_tags(self, instance):
    #     return instance.topic_tags.all()
    # def get_locations(self, instance):
    #     return instance.locations.all()
    # def get_socials(self, instance):
    #     return instance.socials.all()

    class Meta:
        model = Influencers
        fields = (
            "id",
            "influencer_code",
            "name",
            "country",
            "rating",
            "reach",
            "relevance",
            "resonance",
            "description",
            "careers",
            "categories",
            "topic_tags",
            "locations",
            "socials",
            # "refer",
        )
        read_only_fields = (
            "id",
            "influencer_code",
        )
