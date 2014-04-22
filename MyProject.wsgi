import os
import sys	
sys.path.append('/var/www/getip.com/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'MyProject.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
