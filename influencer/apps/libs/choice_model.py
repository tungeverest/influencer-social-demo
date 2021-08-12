import pytz
TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

ACTION_TYPES = (
    (u'CLICK', 'Click'),
    (u'VIEW', 'View'),
    (u'LIKE', 'Like'),
    (u'COMMENT', 'Comment'),
    (u'SHARE', 'Share'),
)

POST_TYPES = (
    (u'CONTENT', 'Click'),
    (u'STATUS', 'Status'),
    (u'VIDEO', 'Video'),
    (u'STREAM', 'Stream'),
    (u'IMAGE', 'Image'),
)

PROFILE_TYPES = (
    (u'USER', 'User'),
    (u'STAFF', 'Staff'),
    (u'MANAGER', 'Manager'),
    (u'ADMIN', 'Admin'),
)

EMPLOYEE_ROLES = (
    (u'USER', 'User'),
    (u'STAFF', 'Staff'),
    (u'MANAGER', 'Manager'),
    (u'ADMIN', 'Admin'),
)
