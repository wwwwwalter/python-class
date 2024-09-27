import sys
import traceback

try:
    x = int(input("input:"))
    print("30/x=",30/x)
except:
    print(sys.exc_info())
    traceback.print_tb(sys.exc_info()[2])
    print("其他异常")