from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from influencer.apps.users.models import UserModel, Employee
from influencer.apps.users.serializers import (
    UserSerializer, EmployeeSerializer
)

# Create your views here.
class UserListViewAPI(generics.ListAPIView):
    permission_classes  = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
