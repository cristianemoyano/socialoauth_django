"""
INTEGRATE EVENTBRITE OAUTH LOGIN IN OUR DJANGO PROJECT
by Cristian Moyano

"""

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socialauth.settings")

application = get_wsgi_application()



project_folder = os.path.expanduser('~/socialauth')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))
