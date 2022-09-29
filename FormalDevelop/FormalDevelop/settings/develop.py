from .base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DEBUG = True
DATABASES = {
    'default': {
'ENGINE': 'django.db.backends.mysql',
        'NAME': 'formdevel',
        'USER': 'root',
        'PASSWORD': '666666',
        'HOSTS': '192.168.163.128',
        'PORT': 3306,
        'OPTIONS': {
            'autocommit': True,
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}
