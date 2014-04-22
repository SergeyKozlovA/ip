"""
WSGI config for ip project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
current_path = os.path.dirname(__file__)
sys.path.append(os.path.join(current_path, '..'))
sys.path.append(current_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ip.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
