import logging

from logging import handlers, Logger

import os
from datetime import datetime

from selenium.webdriver.remote.remote_connection import LOGGER

project_path = os.path.abspath(os.path.dirname(__file__))

# Set WARNING level for webdriver remote connection logger

LOGGER.setLevel(logging.WARNING)

folder = 'logs'
log_path = ''
log_name = '{}_Android_TEST.log'
log_worker_id = None

date_format = '%m-%d-%Y_%H_%M_%S'
name_format = \
    '[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)s] - %(message)s'

# create folder if not exists

if not os.path.exists(log_path):
    log_path = os.path.join(project_path, folder)
    if not os.path.exists(log_path):
        os.makedirs(log_path)

file_name = os.path.join(log_path, log_name)

# Create logger

log: Logger = logging.getLogger('nynja')
log.setLevel(logging.DEBUG)

fmt = logging.Formatter(name_format, date_format)
console_handler = logging.StreamHandler()
file_handler = \
    handlers.RotatingFileHandler(filename=datetime.now().strftime(file_name.format(date_format)),
                                 maxBytes=1048576 * 5, backupCount=7)
console_handler.setFormatter(fmt)
file_handler.setFormatter(fmt)

log.addHandler(console_handler)
log.addHandler(file_handler)


def set_worker_id(worker_id):
    global log_worker_id

    new_name_format = \
        '[%(asctime)s] [{}] [%(levelname)s] [%(filename)s:%(lineno)s] - %(message)s'.format(worker_id)

    if not log_worker_id:
        new_fmt = logging.Formatter(new_name_format, date_format)
        console_handler.setFormatter(new_fmt)
        file_handler.setFormatter(new_fmt)
        log.addHandler(console_handler)
        log.addHandler(file_handler)
        log_worker_id = worker_id
