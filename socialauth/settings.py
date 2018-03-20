"""
Django settings for socialauth project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n)=d7z8y$syja_jc*znz4djgc#$605mq%zjy*o12mmibxu6q8b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'events',
    # add social app
    'social_django',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # add middleware
     'social_django.middleware.SocialAuthExceptionMiddleware',
]

# add AUTHENTICATION_BACKENDS
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.eventbrite.EventbriteOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
)
# aditional parameters

# REDIRECT
SOCIAL_AUTH_LOGIN_REDIRECT_URL = ['/events/all/']

# ENVIRON
# command: export your_key='your_secret'
GITHUB_KEY = os.environ['SOCIAL_AUTH_GITHUB_KEY']
GITHUB_SECRET = os.environ['SOCIAL_AUTH_GITHUB_SECRET']

# ENVIRON
EVENTBRITE_KEY = os.environ['SOCIAL_AUTH_EVENTBRITE_KEY']
EVENTBRITE_SECRET = os.environ['SOCIAL_AUTH_EVENTBRITE_SECRET']

SOCIAL_AUTH_GITHUB_KEY = GITHUB_KEY
SOCIAL_AUTH_GITHUB_SECRET = GITHUB_SECRET
# SOCIAL_AUTH_GITHUB_SCOPE = ['email']

# local
SOCIAL_AUTH_EVENTBRITE_KEY = EVENTBRITE_KEY
SOCIAL_AUTH_EVENTBRITE_SECRET = EVENTBRITE_SECRET
# SOCIAL_AUTH_EVENTBRITE_SCOPE = ['email']

# heroku
# SOCIAL_AUTH_EVENTBRITE_KEY = 'K7QIGYRZXF7X6KQH5M'
# SOCIAL_AUTH_EVENTBRITE_SECRET = '2LYIHHBRS4Q5RWRZNTIQBHQVL46DQGUDOLYRTPKEYT6XTQO7JW'
# SOCIAL_AUTH_EVENTBRITE_SCOPE = ['email']

ROOT_URLCONF = 'socialauth.urls'

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

                # add social context precessors
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',


            ],
        },
    },
]

WSGI_APPLICATION = 'socialauth.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Mendoza'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
