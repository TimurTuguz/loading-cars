import logging.config
from os import environ
from os.path import abspath, dirname, join, exists
from dotenv import load_dotenv


BASE_DIR = abspath(dirname(__file__))
LOG_DIR = join(BASE_DIR, '../log')
LOG_FILE = join(LOG_DIR, 'log')

DOTENV_PATH = join(BASE_DIR, '../.env')
if exists(DOTENV_PATH):
    load_dotenv(DOTENV_PATH)


DB_CONFIG = {
    'host': environ.get('DB_HOST'),
    'database': environ.get('DB_BASE'),
    'user': environ.get('DB_USER'),
    'password': environ.get('DB_PASSWORD'),
    'port': environ.get('DB_PORT')
}

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s(%(name)s) in (%(filename)s:%(lineno)d): %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'level': logging.INFO,
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'file_log': {
            'level': logging.INFO,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': LOG_FILE,
            'backupCount': 2,
            'formatter': 'default',
            'encoding': 'utf-8'
        }
    },
    'loggers': {
        'loading-cars': {
            'level': logging.INFO,
            'handlers': ['file_log', 'console']
        }
    }
}
