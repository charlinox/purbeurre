from default import *

ALLOWED_HOSTS = ['127.0.0.1']

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbpurbeurre',
        'USER': 'charlinox',
        'PASSWORD': os.environ.get('PWDDB_LOCAL'),
        'HOST': '',
        'PORT': os.environ.get('PORT_DB'),
    }
}

INSTALLED_APPS.append("django_extensions")
