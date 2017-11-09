import os


def create_file(file_name):
    """
    A method that will create a file.
    """
    # check if the file already exists
    if not os.path.exists(file_name):
        try:
            open(file_name, 'w')
        except:
            print 'error'


create_file('thingzzz.txt')
create_file('morethingzzz.txt')
