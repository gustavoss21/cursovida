"""
Django settings for cursoVida project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os.path
from pathlib import Path
from re import T
import dj_database_url
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5248$&4&!mb72&xm*x3yw^_dj+*(p6)uk0jlni^!h7snhmi4az'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'produto.apps.ProdutoConfig',
    'contato',
    'core',
    'lista',
    'django.contrib.humanize',
    'django_bootstrap5',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cursoVida.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS':True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cursoVida.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bd_cursovida',
        'USER': 'gustavoroot',
        'PASSWORD': '991465393gs',
        'HOST': 'pgcursovida',
        'PORT': '5432',
    }
}
"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'mydatabase',
    }
}"""
"""DATABASES = {
    'default': dj_database_url.config()
}"""


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# usuario customizado
AUTH_USER_MODEL = 'core.CustomUsuario'
# redirects
LOGOUT_REDIRECT_URL = 'pagina-inicial'
LOGIN_REDIRECT_URL = 'pagina-inicial'

MESSAGE_TAGS = {
    #         messages.DEBUG: 'alert-secondary',
    #         messages.INFO: 'alert-secondary',
    messages.SUCCESS: 'info',
    #         messages.WARNING: 'alert-warning',
    messages.ERROR: 'danger',
}

SESSION_COOKIE_AGE = 60*60*24*7
SESSION_SAVE_EVERY_REQUEST = False

# DEFINIÇOES PARA ENVIO DE E-MAIL

#se nao tiver um host de e-mail
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#se tiver o host de e-mail
# EMAIL_HOST = 'localHost'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'meu-dominio.com'
# EMAIL_HOST_PASSWORD = 12345678
# EMAIL_USE_TLS = True
