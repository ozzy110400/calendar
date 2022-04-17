from __future__ import absolute_import, unicode_literals
from notifications.celery import app


@app.task
def add(x, y):
    return x + y
