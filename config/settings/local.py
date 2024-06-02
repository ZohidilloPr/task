from config.settings.base import *

SECRET_KEY = env('SECRET_KEY')
DEBUG = env("DEBUG")
ALLOWED_HOSTS = str(env("DJANGO_ALLOWED_HOSTS")).split(",")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASS"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")


ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'http://elasticsearch:9200'
    },
}
