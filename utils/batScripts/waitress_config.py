import os
import sys

virtual_env_parent_directory = os.path.dirname(os.environ['VIRTUAL_ENV'])

sys.path.append(virtual_env_parent_directory)  # nopep8
from waitress import serve  # nopep8
from Saint_Stephen_School.wsgi import application  # nopep8
from utils.get_local_ipaddress import get_ip_address  # nopep8
import logging  # nopep8


options = {
    'host': '127.0.0.1',
    'port': 8000,
    'threads': 1,
    'channel_timeout': 30,
    'connection_limit': 250
}

if __name__ == '__main__':
  logger = logging.getLogger('waitress')
  logging.basicConfig(
      filename='utils/batScripts/deployLogs/waitress.log',
      level=logging.INFO,
  )
  serve(application, **options)
