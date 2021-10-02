import random
import time

from celery import shared_task

@shared_task
def generate_random_num():
    number = random.randint(0,1001)
    time.sleep(100)
    return number
       