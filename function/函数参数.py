def add(a, b):
    print("add")
    return a + b


def multi(a, b):
    print("multi")
    return a * b


def my_def(a, b, dis):
    return dis(a, b)


print(my_def(3, 4, add))
print(my_def(3, 4, multi))
