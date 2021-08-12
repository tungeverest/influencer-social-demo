from django.contrib import admin
from .models import (
    Influencers, Social, TopicTag, Location, Career,
    InfluencerCareers, InfluencerCategory, Category,
    InfluencerTopicTag, InfluencerSocial, InfluencerLocation
)

# Register your models here.

@admin.register(
    Influencers, Social, TopicTag, Location, Career,
    InfluencerCareers, InfluencerCategory, Category,
    InfluencerTopicTag, InfluencerSocial, InfluencerLocation
)
class InfluencersAdmin(admin.ModelAdmin):
    pass