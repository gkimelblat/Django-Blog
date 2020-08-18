import os
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '6c5742422b5afc8b3c75c07c48a17a44d3d197fa72de6084'
DEBUG = True

EMAIL_HOST_USER = 'gabrielkni2@gmail.com'
EMAIL_HOST_PASSWORD = 'everythingbelongsto1'
AWS_ACCESS_KEY_ID='AKIAQDOB5Q2BJDJMFM6D'
AWS_SECRET_ACCESS_KEY='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'
AWS_STORAGE_BUCKET_NAME='gherman-first-django'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
