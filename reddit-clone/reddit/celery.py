from celery import Celery

from reddit import settings

__all__ = ("celery",)

celery = Celery(
    main=__name__, backend=settings.CELERY_BACKEND, broker=settings.CELERY_BROKER
)

if __name__ == "__main__":
    celery.start()
