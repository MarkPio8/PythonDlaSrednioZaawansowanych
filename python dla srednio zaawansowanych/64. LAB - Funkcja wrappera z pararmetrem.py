import os,functools
from  datetime import  datetime as dt

def wrapper_with_log_file(logged_action, log_file_path):

    def wrapper_with_log_to_known_file(func):

        def the_real_wrapper(path):

            f = open(log_file_path,"a")
            f.write("Action {} executed on {} on {}".format(logged_action,path,dt.now().strftime("%Y-%m-%d-%H:%M:%S")))
            f.close()
            return func(path)
        return the_real_wrapper
    return wrapper_with_log_to_known_file

@wrapper_with_log_file('FILE_CREATE',r'c:/temp/file_create.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")

@wrapper_with_log_file('FILE_DELETE',r'c:/temp/file_delete.txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'c:\temp\dummy_file.txt')
delete_file(r'c:\temp\dummy_file.txt')
create_file(r'c:\temp\dummy_file.txt')
delete_file(r'c:\temp\dummy_file.txt')