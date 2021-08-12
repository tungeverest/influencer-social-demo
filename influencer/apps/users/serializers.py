from time import time
from django.db import models
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import empty
from rest_framework.validators import UniqueTogetherValidator
from django.conf import settings
from django.db import transaction
from django.utils.translation import ugettext as _
from .models import (
    UserModel, Employee
)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = (
            "id",
            "username",
            "email",
            "fullname",
            "phone",
            "avatar",
            "manager_id",
            "is_verify",
            "user_type",
            "is_staff",
            "is_active",
            "points",
            "rank_user",
            "created_time",
            "updated_time",
            "last_login",
            "last_change_password",
            "country",
            "user_code",
            "invite_code",
            "invite_by",
            "lang",
            "currency",
            "timezone",
            "date_joined"
        )
        read_only_fields = (
            "id",
            "email",
            "country",
            "user_code",
            "date_joined",
        )


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            "id",
            "user",
            "staff_code",
            "department",
            "role",
            "is_active",
        )
        read_only_fields = (
            "id"
        )
