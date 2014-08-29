from kombu import Connection
from kombu.pools import producers


class PoolPublisher(object):
    def __init__(self):
        self.pool = Connection('librabbitmq://guest:guest@localhost:5672//').Pool(10)

    def publish(self, payload, exchange, routing_key=''):
        with self.pool.acquire(block=True) as connection:
            with producers[connection].acquire(block=True) as producer:
                producer.publish(payload, exchange=exchange, routing_key=routing_key)
