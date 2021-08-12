from django.urls import path
from influencer.apps.users.views import (
    UserListViewAPI
)

urlpatterns = [
    path("users/", UserListViewAPI.as_view(), name="user-list"),
    # path(
    #     "customs-declaration/<str:bsin>/",
    #     ProductCustomsDeclarationList.as_view(),
    #     name="product-customs-declaration"
    # )
]
