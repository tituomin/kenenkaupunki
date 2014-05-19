"""
Django settings for kenenkaupunki project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h9#10&9#x=9ih9vy+m8$m)q*ne1z2$59xk19%_b(l!a@cuwqa-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'corsheaders',
    'modeltranslation',
    'munigeo',
    'south',
    'rest_framework',
    'geoanswers',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'geoanswers.cache_middleware.MaxAgeMiddleware'
)

ROOT_URLCONF = 'kenenkaupunki.urls'

WSGI_APPLICATION = 'kenenkaupunki.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'kenenkaupunki',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'vagrant',
        'PASSWORD': 'vagrant',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

gettext = lambda s: s
LANGUAGES = (
    ('fi', gettext('Finnish')),
    ('sv', gettext('Swedish')),
    ('en', gettext('English')),

)
LANGUAGE_CODE = 'fi'
MODELTRANSLATION_DEFAULT_LANGUAGE = LANGUAGE_CODE

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

REST_FRAMEWORK = {
    # 'PAGINATE_BY': 20,
    # 'PAGINATE_BY_PARAM': 'page_size',
    # 'MAX_PAGINATE_BY': 1000,
#    'URL_FIELD_NAME': 'resource_uri',
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}


CORS_ORIGIN_ALLOW_ALL = True


