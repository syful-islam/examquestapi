"""
Django settings for samapi project.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

BASE_URL = config('BASE_URL')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost').split(',')

CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOW_METHODS = [
#     "GET",
#     "POST",
#     "PUT",
#     "PATCH",
#     "DELETE",
#     "OPTIONS",
# ]

# CORS_ALLOW_HEADERS = [
#     "content-type",
#     "authorization",
#     "x-requested-with",
# ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'oauth2_provider',
    'corsheaders',
    'drf_yasg',
    'app',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'app.modules.utils.audit_service.AuditServiceMiddleware',
    # Add your custom middleware here
    'app.middleware.ThreadLocalMiddleware.ThreadLocalMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # OAuth2 authentication
        'rest_framework.authentication.SessionAuthentication',  # Optional for browser-based login
        # 'app.modules.auth.service.TokenAuthWithSubscriber',
    ),
    # enable this part to apply authentication globally for all views
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# Django OAuth Toolkit settings
OAUTH2_PROVIDER = {
    # 'SCOPES': {
    #     'read': 'Read scope',
    #     'write': 'Write scope',
    #     'groups': 'Access to your groups',
    # },
    'ACCESS_TOKEN_EXPIRE_SECONDS': 3600,  # Token expiration time (1 hour)
    'ALLOWED_GRANT_TYPES': ['password', 'authorization_code', 'client_credentials', 'refresh_token'],
    'ALLOW_PUBLIC_CLIENTS': True,  # Required for password grant in some cases
}
AUTH_USER_MODEL = 'app.EQUser'

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Limit the maximum size of a request body to 20MB (20 * 1024 * 1024 bytes)
DATA_UPLOAD_MAX_MEMORY_SIZE = 20 * 1024 * 1024

# Optional: Limit individual file upload size (custom validation)
FILE_UPLOAD_MAX_MEMORY_SIZE = 20 * 1024 * 1024

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.zoho.com'  # For personal users; use 'smtppro.zoho.com' for organization users
EMAIL_PORT = 587
EMAIL_USE_TLS = True  # Use False if using port 465 with SSL
# EMAIL_USE_SSL = True  # Uncomment and set to True if using port 465
EMAIL_HOST_USER = 'otp@autonoming.com'  # Your Zoho email address
EMAIL_HOST_PASSWORD = 'tvqMLujWm3Sn'  # Your application-specific password
EMAIL_FROM_NAME = "SAM App OTP"

# OTP Configuration
OTP_LENGTH = 6
OTP_EXPIRY_MINUTES = 30

LOG_DIR = BASE_DIR / "logs"  # Or any custom path

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'