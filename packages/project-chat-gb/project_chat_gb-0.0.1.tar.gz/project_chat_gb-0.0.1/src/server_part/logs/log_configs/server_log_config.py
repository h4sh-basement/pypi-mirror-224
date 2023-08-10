import os
import logging
from logging import handlers

logger = logging.getLogger('app.server')

log_file = os.path.abspath(os.path.join(os.getcwd())) + '/logs/log_files/app.server.log'

formatter = logging.Formatter('%(asctime)s  %(levelname)-8s  %(module)-10s %(message)s')

file_handler = handlers.TimedRotatingFileHandler(log_file, when='M', interval=20, encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    logger.info('test write log')
    logger.critical('critical write log')