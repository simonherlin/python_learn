"""
    Goodies of the Python Standard Library
"""
# datetimes
import datetime as dt

local_now = dt.datetime.now()
print('local now: {}'.format(local_now))

utc_now = dt.datetime.utcnow()
print('utc now: {}'.format(utc_now))

# You can access any value separately:
print('{} {} {} {} {} {}'.format(local_now.year, local_now.month,
                                 local_now.day, local_now.hour,
                                 local_now.minute, local_now.second))

print('date: {}'.format(local_now.date()))
print('time: {}'.format(local_now.time()))

# strftime()
formatted1 = local_now.strftime('%Y/%m/%d-%H:%M:%S')
print(formatted1)

formatted2 = local_now.strftime('date: %Y-%m-%d time:%H:%M:%S')
print(formatted2)

# strptime()
my_dt = dt.datetime.strptime('2000-01-01 10:00:00', '%Y-%m-%d %H:%M:%S')
print('my_dt: {}'.format(my_dt))

# timedelta
tomorrow = local_now + dt.timedelta(days=1)
print('tomorrow this time: {}'.format(tomorrow))

delta = tomorrow - local_now
print('tomorrow - now = {}'.format(delta))
print('days: {}, seconds: {}'.format(delta.days, delta.seconds))
print('total seconds: {}'.format(delta.total_seconds()))

# Working with timezones
import sys
!{sys.executable} -m pip install pytz
import datetime as dt
import pytz

naive_utc_now = dt.datetime.utcnow()
print('naive utc now: {}, tzinfo: {}'.format(naive_utc_now, naive_utc_now.tzinfo))

# Localizing naive datetimes
UTC_TZ = pytz.timezone('UTC')
utc_now = UTC_TZ.localize(naive_utc_now)
print('utc now: {}, tzinfo: {}'.format(utc_now, utc_now.tzinfo))

# Converting localized datetimes to different timezone
PARIS_TZ = pytz.timezone('Europe/Paris')
paris_now = PARIS_TZ.normalize(utc_now)
print('Paris: {}, tzinfo: {}'.format(paris_now, paris_now.tzinfo))

NEW_YORK_TZ = pytz.timezone('America/New_York')
ny_now = NEW_YORK_TZ.normalize(utc_now)
print('New York: {}, tzinfo: {}'.format(ny_now, ny_now.tzinfo))

# logging


import logging
# Handy way for getting a dedicated logger for every module separately
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

logger.debug('This is debug')
logger.info('This is info')
logger.warning('This is warning')
logger.error('This is error')
logger.critical('This is critical')

# Logging expections
try:
    path_calculation = 1 / 0
except ZeroDivisionError:
    logging.exception('All went south in my calculation')

import os

# This is only required for Jupyter notebook environment
from importlib import reload
reload(logging)

logger = logging.getLogger('MyFileLogger')

# Let's define a file_handler for our logger
log_path = os.path.join(os.getcwd(), 'my_log.txt')
file_handler = logging.FileHandler(log_path)

# And a nice format
formatter = logging.Formatter('%(asctime)s | %(name)-12s | %(levelname)-10s | %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# If you want to see it also in the console, add another handler for it
# logger.addHandler(logging.StreamHandler())

logger.warning('Oops something is going to happen')
logger.error('John Doe visits our place')

# random for random number generation
import random

rand_int = random.randint(1, 100)
print('random integer between 1-100: {}'.format(rand_int))

rand = random.random()
print('random float between 0-1: {}'.format(rand))

random.seed(5)  # Setting the seed

# Let's print 10 random numbers
for _ in range(10):
    print(random.random())

# re for regular expressions
import re

secret_code = 'qwret 8sfg12f5 fd09f_df'
# "r" at the beginning means raw format, use it with regular expression patterns
search_pattern = r'(g12)' 

match = re.search(search_pattern, secret_code)
print('match: {}'.format(match))
print('match.group(): {}'.format(match.group()))

numbers_pattern = r'[0-9]'
numbers_match = re.findall(numbers_pattern, secret_code)
print('numbers: {}'.format(numbers_match))

def validate_only_lower_case_letters(to_validate):
    pattern = r'^[a-z]+$'
    return bool(re.match(pattern, to_validate))

print(validate_only_lower_case_letters('thisshouldbeok'))
print(validate_only_lower_case_letters('thisshould notbeok'))
print(validate_only_lower_case_letters('Thisshouldnotbeok'))
print(validate_only_lower_case_letters('thisshouldnotbeok1'))
print(validate_only_lower_case_letters(''))
