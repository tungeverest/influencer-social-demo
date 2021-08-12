import json
import jwt
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.utils.encoding import smart_text
from django.utils.six import text_type
from django.utils.translation import activate
from django.utils.translation import ugettext_lazy as _

from rest_framework import HTTP_HEADER_ENCODING, exceptions, status
from rest_framework.authentication import (
    BaseAuthentication, TokenAuthentication, get_authorization_header
)
from rest_framework_jwt.settings import api_settings

User = get_user_model()
jwt_decode_handler =  api_settings.JWT_DECODE_HANDLER
auth_header_prefix =  api_settings.JWT_AUTH_HEADER_PREFIX


class CustomTokenAuthentication(BaseAuthentication):
    """
    Token based authentication using the JSON Web Token standard.
    """

    def authenticate(self, request):
        """
        Returns a two-tuple of `User` and token if a valid signature has been
        supplied using JWT-based authentication.  Otherwise returns `None`.
        """
        print('2323232323')
        jwt_value = self.get_jwt_value(request)

        if jwt_value is None:
            return None

        try:
            payload = jwt_decode_handler(jwt_value)
        except jwt.ExpiredSignature:
            msg = _('[JWT] Signature has expired.')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = _('[JWT] Error decoding signature.')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed()

        user = self.authenticate_credentials(payload)

        return user, payload

    def authenticate_credentials(self, payload):
        """
        Returns an active user that matches the payload's user id and email.
        """
        print(payload)
        email = payload['email']
        user_id = payload['user_id']
        exp = payload['exp']
        msg = {'Error': "Token mismatch",'status' :"401"}
        try:

            user = User.objects.get(
                email=email,
                id=user_id,
            )
            if not user:
                msg = _('Invalid payload.')
                raise exceptions.AuthenticationFailed(msg)

        except (
            jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError
        ):
            msg = _('Token is invalid.')
            raise exceptions.AuthenticationFailed(msg)
        except User.DoesNotExist:
            msg = _('User account not exist.')
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            raise exceptions.AuthenticationFailed(
                _('User account is disabled.')
            )

        return user

    def get_jwt_value(self, request):
        auth = get_authorization_header(request).split()

        if not auth:
            return None

        if smart_text(auth[0].upper()) != auth_header_prefix:
            return None

        if len(auth) == 1:
            msg = _('Invalid Authorization header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid Authorization header. Credentials string '
                    'should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)
        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return token
