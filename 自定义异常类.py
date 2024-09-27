import sys
import traceback


class InputError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "{} is invalid input".format(repr(self.value))


try:
    raise InputError(100)
except InputError as e:
    # print(f'error:{e}')
    # traceback.print_exc()
    print(traceback.format_exc())
