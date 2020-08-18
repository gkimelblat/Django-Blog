import os
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ''
DEBUG = True

EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''
AWS_STORAGE_BUCKET_NAME=''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
