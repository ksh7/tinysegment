from __future__ import absolute_import, unicode_literals

import os

from django.conf import settings

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.broker_url = os.environ.get('REDIS_URL', f"redis://{os.getenv('CELERYAPP_HOST')}:6379")

app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

app.conf.beat_schedule = {
    'check-everyhour-contrab': {
        'task': 'scheduled_weather_notifications',
        'schedule': crontab(hour='*/1', minute=0,),
    },
}