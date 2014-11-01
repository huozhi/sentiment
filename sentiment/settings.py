"""
Django settings for sentiment project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# import mongoengine

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=m0e_$a4s_n8p^0#2h^zx52x#z2&zej(lc#6)i#ray*(!@meud'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'template'),
)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mood',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sentiment.urls'

WSGI_APPLICATION = 'sentiment.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


# AUTH_USER_MODEL = 'mongo_auth.MongoUser'
# MONGOENGINE_USER_DOCUMENT = 'mongoengine.django.auth.User'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sentiment',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': 3306
    }
}

# AUTHENTICATION_BACKENDS = (
#     'mongoengine.django.auth.MongoEngineBackend',
# )

# # session
# SESSION_EGINE = 'mongoengine.django.sessions'
# SESSION_SERIALIZER = 'mongoengine.django.sessions.BSONSerializer'


# _MONGODB_USER = 'root'
# _MONGODB_PASSWD = 'root'
# _MONGODB_HOST = 'localhost'
# _MONGODB_NAME = 'sentiment'
# _MONGODB_DATABASE_HOST = \
#     'mongodb://%s:%s@%s/%s' \
#     % (_MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_NAME)

# mongoengine.connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL.replace('/', ''))

STATICFILES_DIRS = (
    'static',
    'media',
)

MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'
