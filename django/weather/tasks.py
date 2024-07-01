import logging

from celery import shared_task
from redis import Redis

from django.conf import settings

LOGGER = logging.getLogger(__file__)


@shared_task
def redis_weather_listener() -> None:
    try:
        r = Redis(
            host="redis",
            port=6379,
            decode_responses=True,
        )

        test_redis = r.get("test")
        LOGGER.info(test_redis)

    except Exception as e:
        LOGGER.exception(e)