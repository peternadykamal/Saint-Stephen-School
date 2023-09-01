"""
Django settings for Saint_Stephen_School project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import socket
from pathlib import Path

from utils.get_current_git_branch import get_current_git_branch
from utils.get_env_value import get_env_value
from utils.get_local_ipaddress import get_ip_address

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j76sdd(dc+wa=(d8prvwk311l@4g=dvgzs$d-9(f08asj5!x!)'

# SECURITY WARNING: don't run with debug turned on in production!
if get_current_git_branch() == 'main':
  DEBUG = False
else:
  DEBUG = True

# DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', get_ip_address(),
                 'saint-stephen-school.peternady.social',]
CSRF_TRUSTED_ORIGINS = [
    'https://saint-stephen-school.peternady.social', 'http://127.0.0.1', f'http://{get_ip_address()}']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'livereload',
    'django.contrib.staticfiles',

    'landing.apps.LandingConfig',
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'users.middleware.UserProfileMiddleware',
    'livereload.middleware.LiveReloadScript',
]

ROOT_URLCONF = 'Saint_Stephen_School.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'Saint_Stephen_School.context_processors.navigation_config',
            ],
        },
    },
]

WSGI_APPLICATION = 'Saint_Stephen_School.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Retrieve the values from environment variables
if DEBUG == True:
  db_host = get_env_value("DB_HOST_DEV")
  db_user = get_env_value("DB_USER_DEV")
  db_password = get_env_value("DB_PASSWORD_DEV")
  db_name = get_env_value("DB_NAME_DEV")
else:
  db_host = get_env_value("DB_HOST_PROD")
  db_user = get_env_value("DB_USER_PROD")
  db_password = get_env_value("DB_PASSWORD_PROD")
  db_name = get_env_value("DB_NAME_PROD")

# if the host is peter-nady, then use the local database
if socket.gethostname() == 'peter-nady':
  db_host = "peter-nady"
  db_user = get_env_value("DB_USER_DEV")
  db_password = get_env_value("DB_PASSWORD_DEV")
  db_name = get_env_value("DB_NAME_DEV")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Cairo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'files/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# because i use javascript modules in some cases, which because of the new es6 standard,
# the browser will not load them if they are not served with the correct mime type so i need to give them type="module"
# in this case yeah the browser become able to read the files correctly but django can't identity the module type
# so in this case i need to explicitly tell django that each file with .js extension is a javascript module
if DEBUG:
  import mimetypes
  mimetypes.add_type("application/javascript", ".js", True)

# This tell django where to uplod user generated content
STATIC_ROOT = os.path.join(BASE_DIR, 'deployedStaticFiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'files')
# python manage.py collectstatic

ORIGINAL_PROFILE_PICTURES_FOLDER = os.path.join(
    MEDIA_ROOT, 'images', 'profiles', 'original')
MANUALLY_CROPPED_PATHES_CSV = os.path.join(
    MEDIA_ROOT, 'images', 'profiles', 'error_images.csv')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
