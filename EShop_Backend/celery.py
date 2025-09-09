from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EShop_Backend.settings')

app = Celery('EShop_Backend')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    

app.conf.beat_schedule = {
    'delete-unverified-every-hour': {
        'task': 'Authentication.tasks.delete_unverified_users',
        'schedule': crontab(minute=0, hour='*'),  # runs every hour
    },
}
