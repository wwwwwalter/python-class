# Python生成器close()方法
# 当程序在生成器函数中遇到 yield 语句暂停运行时，
# 此时如果调用 close() 方法，会阻止生成器函数继续执行，
# 该函数会在程序停止运行的位置抛出 GeneratorExit 异常。

def foo():
    try:
        yield 1
    except GeneratorExit:
        print("GeneratorExit")

    print("其他代码可以继续执行")

f = foo()

print(next(f)) # yield 1
f.close()

# 两个注意点
# 虽然通过捕获 GeneratorExit 异常，可以继续执行生成器函数中剩余的代码，
# 但这部分代码中不能再包含 yield 语句，否则程序会抛出 RuntimeError 异常。

# 生成器函数一旦使用 close() 函数停止运行，
# 后续将无法再调用 next() 函数或者 __next__() 方法启动执行，否则会抛出 StopIteration 异常。