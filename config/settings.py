"""
Django settings for config project.
Generated by 'django-admin startproject' using Django 3.2.16.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dot_env = BASE_DIR / ".env"
load_dotenv(dotenv_path=dot_env)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

if DEBUG:
    INTERNAL_IPS = [
        "192.168.1.4",
        "127.0.0.1",
    ]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "markdownify.apps.MarkdownifyConfig",
    "social_django",
    "crispy_forms",
    "debug_toolbar",
    "mainapp",
    "authapp",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "mainapp.context_processors.example.simple_context_processor",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "authapp.CustomUser"
LOGIN_REDIRECT_URL = "mainapp:main_page"
LOGOUT_REDIRECT_URL = "mainapp:main_page"
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

AUTHENTICATION_BACKENDS = (
    "social_core.backends.github.GithubOAuth2",
    "social_core.backends.vk.VKOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

SOCIAL_AUTH_GITHUB_KEY = os.getenv("AUTH_GITHUB_KEY")
SOCIAL_AUTH_GITHUB_SECRET = os.getenv("AUTH_GITHUB_SECRET")

SOCIAL_AUTH_VK_OAUTH2_KEY = os.getenv("AUTH_VK_OAUTH2_KEY")
SOCIAL_AUTH_VK_OAUTH2_SECRET = os.getenv("AUTH_VK_OAUTH2_SECRET")

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Параметры развертывания на сервере / локальные параметры для БД и пути до статики

STATIC_URL = "static/"

if os.getenv("ENV_TYPE") != "local":
    STATIC_ROOT = BASE_DIR / "static"

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "braniac",
            "USER": "django",
            "PASSWORD": "geekbrains",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }
else:
    STATICFILES_DIRS = (BASE_DIR / "static/",)

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

CRISPY_TEMPLATE_PACK = "bootstrap4"

LOG_FILE = BASE_DIR / "var" / "log" / "main_log.log"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {"format": "[%(asctime)s] %(levelname)s %(name)s (%(lineno)d) %(message)s"},
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": LOG_FILE,
            "formatter": "console",
        },
        "console": {"class": "logging.StreamHandler", "formatter": "console"},
    },
    "loggers": {
        "django": {"level": "INFO", "handlers": ["console"]},
        "mainapp": {
            "level": "DEBUG",
            "handlers": ["file"],
        },
    },
}

# CELERY
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"


# Read about sending email:
#   https://docs.djangoproject.com/en/3.2/topics/email/

# Full list of email settings:
#   https://docs.djangoproject.com/en/3.2/ref/settings/#email
# EMAIL_HOST = "localhost"
# EMAIL_PORT = "25"

# For debugging: python -m smtpd -n -c DebuggingServer localhost:25
# EMAIL_HOST_USER = "django@geekshop.local"
# EMAIL_HOST_PASSWORD = "geekshop"
# EMAIL_USE_SSL = False
# If server support TLS:
# EMAIL_USE_TLS = True

# Email as files for debug
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = "var/email-messages/"


# In the end of file
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

LOCALE_PATHS = [BASE_DIR / "locale"]

SELENIUM_DRIVER_PATH_FF = BASE_DIR / "var" / "selenium" / "geckodriver"
