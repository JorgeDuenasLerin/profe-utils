from .base import *
import json

with open(BASE_DIR / 'secrets.json') as f:
    config = json.load(f)

ALLOWED_HOSTS = ['localhost', 'iesgestionweb.duenaslerin.com']
DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = config["databases"]
SECRET_KEY = config["secret"]

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
