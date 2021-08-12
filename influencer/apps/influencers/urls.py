from django.urls import path
from influencer.apps.influencers.views import (
    InfluencerListViewAPI
)

urlpatterns = [
    path("influencers/", InfluencerListViewAPI.as_view(), name="influencers-list"),
    # path(
    #     "customs-declaration/<str:bsin>/",
    #     ProductCustomsDeclarationList.as_view(),
    #     name="product-customs-declaration"
    # )
]
