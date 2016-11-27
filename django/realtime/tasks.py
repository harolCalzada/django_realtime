import time
from celery import task
import redis

redis_client = redis.StrictRedis(host='redis', port=6379, db=0)


@task(bind=True)
def generate_csv(self):
    print ('entre al generate csv')
    time.sleep(10)
    result = 'http://google.com'
    redis_client.publish(self.request.id, result)
