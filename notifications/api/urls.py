from django.urls import path
from .views import testing_task


urlpatterns = [
    path('celery-test/', testing_task, name='celery_test_url'),
]