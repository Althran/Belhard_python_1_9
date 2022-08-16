"""
Настроить логгирование с модулем logging.

Настроить формат вывода.
Настроить, чтобы вывод шел в файл и в консоль.
Настроить ротацию файла лога по времени (полночь).
"""
import logging
from logging.handlers import TimedRotatingFileHandler

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s')
handler = TimedRotatingFileHandler(filename='app.log', when="midnight")

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
logging.critical('This is critical message')
