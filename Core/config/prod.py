from .dev import *

import django_heroku
django_heroku.settings(locals())

import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)