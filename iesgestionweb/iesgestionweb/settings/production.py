from .base import *
import json

with open(BASE_DIR / 'secrets.json') as f:
    config = json.load(f)

ALLOWED_HOSTS = ['localhost', 'iesgestionweb.duenaslerin.com']
DEBUG = False
DATABASES = config["databases"]
SECRET_KEY = config["secret"]
