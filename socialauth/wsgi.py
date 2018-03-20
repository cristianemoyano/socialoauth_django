"""
WSGI config for socialauth project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socialauth.settings")

application = get_wsgi_application()



project_folder = os.path.expanduser('~/socialauth')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))
