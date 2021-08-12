from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework import exceptions
from influencer.apps.influencers.models import Influencers
from influencer.apps.influencers.serializers import (
    InfluencersSerializer
)
from django.contrib.auth.models import Permission

# Create your views here.
class InfluencerListViewAPI(generics.ListAPIView):
    permission_classes  = (permissions.IsAuthenticated,)
    queryset = Influencers.objects.all()
    serializer_class = InfluencersSerializer

    def get(self, request, *args, **kwargs):
        permissions = Permission.objects.filter(user=self.request.user)
        # print(self.request.user.user_permissions.filter(codename='view_influencers'))
        print(Permission.objects.filter(group__user=self.request.user))
        # if self.request.user.user_permissions.filter(codename='view_influencers'):
        if Permission.objects.filter(group__user=self.request.user, codename='view_influencers'):
            return self.list(request, *args, **kwargs)
        else:
            raise exceptions.PermissionDenied('No permission access')

