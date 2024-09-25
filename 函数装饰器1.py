# @staticmethod、@classmethod 和 @property，
# 其中 staticmethod()、classmethod() 和 property() 都是 Python 的内置函数。


# 装饰器的作用：
# 装饰器是一种设计模式，用于在不修改原函数的基础上增加额外的功能。
# 在 Python 中，装饰器本质上是一个接受函数作为参数的函数，并返回一个新的函数。

# 装饰器的返回值：
# 当装饰器应用于某个函数时，实际上是在函数调用前和调用后增加了额外的行为。
# funA 的返回值 "装饰器函数的返回值" 是 funA 执行完毕后的结果，并不是给 fn 的


def funA(fn):
    def wrapper():
        print("C语言中文网")
        fn()
        print("http://c.biancheng.net")
    return wrapper # 把包装好的新函数返回给fn

@funA
def my_function():
    print("这是被装饰的函数")

my_function()  # 调用被装饰的函数
print(type(my_function)) # function
