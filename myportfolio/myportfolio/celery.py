from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')

app = Celery('myportfolio')

app.conf.enable_utc = False

app.conf.update(timezone = 'Africa/Nairobi')

app.config_from_object(settings, namespace='CELERY')



#Celery Beat Settings
app.conf.beat_schedule = {
    
}
# app.autodiscover_tasks()
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# Configure Celery to use Redis as the broker
app.conf.broker_url = 'redis://127.0.0.1:6379'


