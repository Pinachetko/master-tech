from .base import *


ADMINS = [
    ("PiNaCheT", "costya.badanin2015@yandex.ru"),
]

MANAGERS = [
    ("PiNaCheT", "costya.badanin2015@yandex.ru"),
]

DEBUG = True

APPEND_SLASH = True

DEFAULT_CHARSET = 'utf-8'

DEFAULT_FROM_EMAIL = "costya.badanin2015@yandex.ru"

DEV_ALLOWED_HOSTS = [
    "www.rybinsk-tech.com"
]

ALLOWED_HOSTS.extend(DEV_ALLOWED_HOSTS)

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')

MEDIA_URL = '/media/'


STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static/')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'app/static/'),
)

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEV_APP = [
    "app",
]

INSTALLED_APPS.extend(DEV_APP)

DEV_DATABASES = {
    'default': {
        'NAME': 'tech_db',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'CONN_MAX_AGE': 0,
    }
}

DATABASES.update(DEV_DATABASES)
