def test():
    raise ZeroDivisionError("除数不能为0")

try:
    test()
except ZeroDivisionError as e:
    print(repr(e))
