"""
Exceptions
"""

# custome exceptions
class CustomException(Exception):
    ...

# raise exception

# num = -1
# if num > 0:
#     print("Succesfull")
# else:
#     raise Exception("Failed")


# try catch family

def download_config(file=False):
    if file:
        return "down_loaded_config"
    else:
        raise FileNotFoundError

def default_config():
    return "default_config"

try:
    config = download_config()
except FileNotFoundError:
    config = default_config()
finally:
    # this will always run
    print(config)


# name-bound exceptions
try:
    num = open('number.txt').readline()
except FileNotFoundError as e:
    print(f'Cannot read {e.filename}')

