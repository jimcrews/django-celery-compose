import logging
from django.core.exceptions import ObjectDoesNotExist

from celery import shared_task
from redis import Redis

from .models import Forecast

LOGGER = logging.getLogger(__file__)


@shared_task
def redis_weather_listener() -> None:
    try:
        msg = None

        # connect
        r = Redis(
            host="redis",
            port=6379,
            decode_responses=True,
        )

        # Start from the last message if there is one
        last_msg = None 
        
        try: 
            last_msg = Forecast.objects.latest("date")
        except ObjectDoesNotExist:
            LOGGER.info("no forecast.. get all")

        if last_msg:
            msg = r.xrange("weather:sydney", "("+last_msg.stream_id, "+", 1)
        else:
            msg = r.xrange("weather:sydney", "-", "+", 1)


        LOGGER.info(msg)
        if msg:
            forecast = Forecast(
                stream_id=msg[0][0],
                date=msg[0][1]['date'],
                temperature=msg[0][1]['temperature'],
                summary=msg[0][1]['summary'],
                fire_danger=msg[0][1]['fire_danger']
            )
            forecast.save()

    except Exception as e:
        LOGGER.exception(e)