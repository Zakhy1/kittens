import os

DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': int(os.environ.get('POSTGRES_PORT', '5432')),
        'NAME': os.environ.get('POSTGRES_DB', 'db'),
        'USER': os.environ.get('POSTGRES_USER', 'db_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'qe12332'),
    },
}
