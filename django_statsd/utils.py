import statsd
from django.conf import settings

def get_connection(host=None, port=None, sample_rate=None):
    if not host:
        host = getattr(settings, 'STATSD_HOST', '127.0.0.1')

    if not port:
        port = getattr(settings, 'STATSD_PORT', 8125)

    if not sample_rate:
        sample_rate = getattr(settings, 'STATSD_SAMPLE_RATE', 1.0)

    return statsd.Connection(host, port, sample_rate)

def get_timer(name, connection=None):
    if not connection:
        connection = get_connection()

    return statsd.Timer(name, connection)

def get_client(name, connection=None):
    if not connection:
        connection = get_connection()

    return statsd.Client(name, connection)

