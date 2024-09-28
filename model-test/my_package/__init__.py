'''
http://c.biancheng.net/
创建第一个 Python 包
'''
print('I am in __init__.py')


# my_package
#      ┠── __init__.py
#      ┠── module1.py
#      ┗━━  module2.py


from . import model1
from .model2 import *