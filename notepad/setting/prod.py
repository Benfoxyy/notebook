from notepad.settings import *
from .skey import key

SECRET_KEY = key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR/'static'
STATIC_FILES =[
    BASE_DIR/'static',
]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'