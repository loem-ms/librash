from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Logging setting
LOGGING = {
    'version': 1,
    'disable_existing_logger': False,
    
    # Logger
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        
        'mylibrary': {
            'handler': ['console'],
            'level': 'DEBUG',
        },
    },
    
    # Handler
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev',
        }
    },
    
    # Formatter
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },        
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')