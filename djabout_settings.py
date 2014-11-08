SECRET_KEY = 'NotVerySecretKey'

INSTALLED_APPS = (
    'djabout.maintenance',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

USE_TZ = True

ROOT_URLCONF = 'djabout.maintenance.urls'

APP_VERSION = 'To override'
