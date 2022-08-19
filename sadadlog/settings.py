"""
Django settings for sadadlog project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
#import ldap
#from django_auth_ldap.config import LDAPSearch

#AUTH_LDAP_SERVER_URI = 'ldap://192.168.1.177'
#AUTH_LDAP_BIND_DN = "CN=bind,CN=Users,DC=spsplan,DC=local"
#AUTH_LDAP_BIND_PASSWORD = "aA@@135792468"
#AUTH_LDAP_USER_SEARCH = LDAPSearch(
#            "dc=spsplan,dc=local", ldap.SCOPE_SUBTREE, "sAMAccountName=%(user)s"
#            )

#AUTH_LDAP_USER_ATTR_MAP = {
#            "username": "sAMAccountName",
#                "first_name": "givenName",
#                    "last_name": "sn",
#                        "email": "mail",
#}
#from django_auth_ldap.config import ActiveDirectoryGroupType
#AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
#            "dc=spsplan,dc=local", ldap.SCOPE_SUBTREE, "(objectCategory=Group)"
#            )
#AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType(name_attr="cn")
#AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#            "is_superuser": "CN=NOCLogApp,CN=Users,DC=SPSPLAN,DC=LOCAL",
#            "is_staff": "CN=NOCLogApp,CN=Users,DC=SPSPLAN,DC=LOCAL",
#            }
#AUTH_LDAP_FIND_GROUP_PERMS = True
#AUTH_LDAP_CACHE_GROUPS = True
#AUTH_LDAP_GROUP_CACHE_TIMEOUT = 1  # 1 hour cache

#AUTHENTICATION_BACKENDS = [
#            'django_auth_ldap.backend.LDAPBackend',
#                'django.contrib.auth.backends.ModelBackend',
#]



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ifn=2r$0_zb+l%e*-!3*o*pt+g!lv@%lt%9!k+e34i#fjzbqaz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'log',
    'django_jalali',
    'jalali_date',
    'django_filters',
    'jet',
    'jet.dashboard',
    'simple_history',
    'mathfilters',
    
   
    'crispy_forms',
    
    
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# default settings
JALALI_DATE_DEFAULTS = {
   'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            # loading datepicker
            'admin/js/django_jalali.min.js',
            # OR
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'admin/js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'sadadlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.join('/accounts/templates'))],
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

WSGI_APPLICATION = 'sadadlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

LANGUAGE_CODE = 'en-us'
import locale
locale.setlocale(locale.LC_ALL, "fa_IR.UTF-8")

CACHES = {
        "default":{
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient"
            },
            "KEY_PREFIX":"SADADLOG"
        }
}