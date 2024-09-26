try:
    1/0
except Exception as e:
    print(e)
    print(e.args)
    print(str(e))
    print(repr(e))
    print(type(e))
    print(Exception)

