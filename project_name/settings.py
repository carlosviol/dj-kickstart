# coding: utf-8
"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from decouple import config
from dj_database_url import parse as db_url
from unipath import Path

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

BASE_DIR = Path(__file__).parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['.localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_nose',
    'django_extensions',
    'reversion',
    'django_jenkins',
    'model_mommy',

    '{{ project_name }}.core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + BASE_DIR.child('db.sqlite3'),
        cast=db_url),
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = BASE_DIR.child('static')
STATIC_URL = '/static/'


# Media files (user uploaded files)

MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'


# Django-Jenkins

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.run_csslint',
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_flake8',
    'django_jenkins.tasks.run_sloccount',
)
JENKINS_TEST_RUNNER = 'django_jenkins.runner.CITestSuiteRunner'

PROJECT_APPS = ['{{ project_name }}']
