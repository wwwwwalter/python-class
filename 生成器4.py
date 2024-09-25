# Python生成器throw()方法
# 生成器 throw() 方法的功能是，在生成器函数执行暂停处，抛出一个指定的异常，
# 之后程序会继续执行生成器函数中后续的代码，直到遇到下一个 yield 语句。
# 需要注意的是，如果到剩余代码执行完毕没有遇到下一个 yield 语句，则程序会抛出 StopIteration 异常。

def foo():
    try:
        yield 1
    except ValueError:
        yield 8
        print("捕获到 ValueError") # 消耗掉 yield 8 或者 yield 2
        yield 2
        yield 3 # 从这里继续执行
        yield 4

f = foo()

print(next(f)) # yield 1
f.throw(ValueError) # yield 2
print(next(f)) # yield 3
print(next(f)) # yield 4