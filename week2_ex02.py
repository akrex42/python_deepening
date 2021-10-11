import json
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        obj = func(*args, **kwargs)
        return json.dumps(obj)
    return wrapped


# @to_json
# def get_data():
#     return '42'
#
#
# print(get_data())
