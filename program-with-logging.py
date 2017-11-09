import os # this is a python library module

import logfun # this is the module we wrote


def create_file(file_name):
    """
    A method that will create a file.
    """
    cwd = os.getcwd()
    log_message = 'Creating new file: %s at path: %s' % (file_name, cwd)

    # check if the file already exists
    if not os.path.exists(file_name):
        try:
            open(file_name, 'w')
            logfun.basic_logging(log_message)
        except:
            error_log_message = 'Error: Could not create file: %s.' % file_name
            logfun.basic_logging(error_log_message)

    else: # if the file already exists then log that
        log_message = 'File already exists: %s' % file_name
        logfun.basic_logging(log_message)


create_file('thingzzz.txt')
create_file('morethingzzz.txt')
