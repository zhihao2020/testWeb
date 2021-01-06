"""
Created by zhihao

there will add configure to reload secret contents
"""

from pathlib import Path
import os
from configparser import ConfigParser

cfg = ConfigParser(interpolation=None)
cfg.read('website\config.ini')
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#5dwu)2l0^=%kn#^84dc$_i@+%w*-o-im-3ju8t%d&v87lx%*-e
#with open("website\secret.txt") as f:
#    SECRET_KEY = f.read().strip()

SECRET_KEY = cfg.get('default','SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'HousingProvidenFundStatement',
    'Employeeincomestatement',
   
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

ROOT_URLCONF = 'website.urls'
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE= 60*5
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates'),
            os.path.join(BASE_DIR,'templates/HousingProvidenFundStatement/'),
            os.path.join(BASE_DIR,'templates/Employeeincomestatement')
        ],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': cfg.get('mysql','NAME'),
        'USER':cfg.get('mysql','USER'),
        'PASSWORD':cfg.get('mysql','PASSWORD'),
        'HOST':cfg.get('mysql','HOST'),
        'PORT':cfg.get('mysql','PORT'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

#开发中使用
STATIC_URL = '/static/'
#STATIC_ROOT=os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)


MEDIA_URL='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

