import os

class ZalgoConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')