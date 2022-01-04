import os
import sys
from django.core.wsgi import get_wsgi_application

# add the hellodjango project path into the sys.path
sys.path.append("/home/django/autotests-common/coverage_dashbord/mysite/")

# add the virtualenv site-packages path to the sys.path
sys.path.append("/home/cto_qa/.local/lib/python3.8/site-packages")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
