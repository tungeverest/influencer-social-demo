import hashlib
import re
import uuid
import time
from os import makedirs, path
from datetime import datetime
from django.conf import settings
from django.utils.timezone import now
from django.utils.translation import ugettext as _
from urllib import parse


def get_uuid(prefix="", suffix="", length=11):
    if length > 11:
        raise ValueError("Maximum uuid length is 11")

    _uuid = str(round(
        uuid.uuid1().int / 1395812391238232312323232232
    ))[:length]

    _uuid = f"{prefix}{_uuid}{suffix}"
    return _uuid