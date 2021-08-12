import os
import pytz
import time
import datetime
import itertools
import random, string

from django.db import models
from django.db.models.deletion import PROTECT, CASCADE, SET_NULL
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import IntegrityError, models, transaction
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
from influencer.apps.libs.choice_model import (
    TIMEZONES, PROFILE_TYPES, EMPLOYEE_ROLES
)
from unixtimestampfield.fields import UnixTimeStampField
# Create your models here.


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User`.

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, username, email, password=None):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    """
    Concrete class of AbstractEmailUser.
    Use this if you don't need to extend EmailUser.
    """

    username = models.CharField(
        db_index=True, max_length=255, blank=True, null=True
    )
    email = models.EmailField(
        _('email address'), max_length=255, unique=True
    )
    is_staff = models.BooleanField(
        _('staff status'), default=False
    )
    is_active = models.BooleanField(
        _('active'), default=True
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(
        max_length=32, blank=True, null=True, unique=True
    )
    avatar = models.CharField(
        unique=True, max_length=255, blank=True, null=True
    )
    manager_id = models.IntegerField(default=0)

    # Xac thuc nhan vien
    is_verify = models.IntegerField(default=0)
    user_type = models.CharField(
        default='USER', choices=PROFILE_TYPES, max_length=16
    )
    #Rank - 0:normal, 1:silver, 2:gold, 3:Diamond
    rank_user = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    created_time = UnixTimeStampField(
        auto_now_add=True, verbose_name=_("Created time")
    )
    updated_time = UnixTimeStampField(
        auto_now=True, verbose_name=_("Updated time")
    )
    last_login = UnixTimeStampField(
        auto_now=True, verbose_name=_("Last logedin time")
    )
    last_change_password = UnixTimeStampField(
        auto_now_add=True, verbose_name=_("Last logedin time")
    )
    country = CountryField(default='VN', blank_label="Select country")
    user_code  = models.IntegerField(default=0, unique=True)
    # Verify user
    invite_code = models.CharField(max_length=10, blank=True, null=True)
    invite_by = models.ForeignKey(
        'self', on_delete=SET_NULL, null=True, blank=True,
        related_name="inviter"
    )

    lang = models.CharField(max_length=2, blank=True, null=True, default='vi')
    currency = models.CharField(max_length=3, default="VND")
    timezone = models.CharField(
        max_length=32, choices=TIMEZONES, default='UTC'
    )
    # payment_type = models.ForeignKey(
    #     Payment, on_delete=SET_NULL, related_name="payments"
    # )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.

        This string is used when a `User` is printed in the console.
        """
        return self.email

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically this would be the user's first and last name. Since we do
        not store the user's real name, we return their username instead.
        """
        return self.username

    def get_short_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically, this would be the user's first name. Since we do not store
        the user's real name, we return their username instead.
        """
        return self.username

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this User."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    #random PIN
    @staticmethod
    def genrate_user_code(number):
        lower = 10**(number-1)
        upper = 10**number - 1
        random_randint = random.randint(lower, upper)
        while UserModel.objects.filter(user_code = random_randint).exists():
            random_randint = UserModel.genrate_user_code(number)

        return random_randint

    def save(self, **kwargs):
        self.user_code = str(UserModel.genrate_user_code(6))
        return super().save(**kwargs)


class Employee(models.Model):
    user = models.ForeignKey(
        UserModel, on_delete=CASCADE, related_name="user_employee"
    )
    staff_code =  models.CharField(max_length=6, unique=True)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=60, choices=EMPLOYEE_ROLES, default='Sale')
    is_active = models.BooleanField(default=False)

    @staticmethod
    def genrate_staff_code(number):
        lower = 10**(number-1)
        upper = 10**number - 1
        random_randint = random.randint(lower, upper)
        while Employee.objects.filter(staff_code = random_randint).exists():
            random_randint = Employee.genrate_staff_code(number)

        return random_randint

    def save(self, **kwargs):
        self.staff_code = str(Employee.genrate_staff_code(6))
        return super().save(**kwargs)

    class Meta:
        db_table = 'employee'
        ordering = ['-id']