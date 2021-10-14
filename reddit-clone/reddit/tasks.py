from celery import Celery

from reddit import settings

__all__ = ("celery",)

celery = Celery(__name__)
celery.conf.result_backend = settings.CELERY_BACKEND
celery.conf.broker_url = settings.CELERY_BROKER

if __name__ == "__main__":
    celery.start()
