"""
A simple logging method.
Note that python has a logging module that you would normally use.
https://docs.python.org/2/howto/logging.html
"""

from datetime import datetime


def basic_logging(msg_to_log):
    """
    Append a log event to the log file with the current date and time.
    """
    with open('log.txt', 'a') as log_file:
        date = datetime.utcnow().isoformat()
        log = '%s [-] %s \n' % (date, msg_to_log) 
        log_file.write(log)
