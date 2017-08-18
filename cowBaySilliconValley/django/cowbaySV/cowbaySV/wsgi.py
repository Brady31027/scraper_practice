"""
WSGI config for cowbaySV project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise #heroku add

onHeroku = False

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cowbaySV.settings")

application = ''
if onHeroku:
	application = DjangoWhiteNoise(application)
else:
	application = get_wsgi_application()


