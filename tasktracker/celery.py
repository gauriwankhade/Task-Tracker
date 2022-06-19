import os

from celery import Celery

# Set teh default Django settings module for teh 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasktracker.settings')

app = Celery('tasktracker')

# Using a string here means teh worker doesn't has to serialize
# teh configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should of a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')