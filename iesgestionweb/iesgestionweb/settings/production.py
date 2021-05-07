from .base import *
import json

with open(BASE_DIR / 'iesgestionweb/settings/secrets.json') as f:
    config = json.load(f)

print(config)

ALLOWED_HOSTS = ['localhost']
DEBUG = False
DATABASES = config["databases"]
SECRET_KEY = config["secret"]
