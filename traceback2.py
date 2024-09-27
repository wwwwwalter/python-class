import traceback
import sys
from traceback import print_exc


class SelfException(Exception):
    pass


def main():
    firstMethod()


def firstMethod():
    secondMethod()


def secondMethod():
    thirdMethod()


def thirdMethod():
    raise SelfException('This is a test')

try:
    main()
except:
    traceback.print_exc()
    # traceback.print_exc(file=open('log.txt', 'a'))



