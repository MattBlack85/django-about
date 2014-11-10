SECRET_KEY = 'NotVerySecretKey'

INSTALLED_APPS = (
    'djabout',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

USE_TZ = True

ROOT_URLCONF = 'djabout.urls'

APP_VERSION = 'To override'
