# 带参数的 send(value) 的用法，
# 其具备 next() 函数的部分功能，即将暂停在 yield 语句出的程序继续执行，
# 但与此同时，该函数还会将 value 值作为 yield 语句返回值赋值给接收者。
# 带参数的 send(value) 无法启动执行生成器函数。
# 程序中第一次使用生成器调用 next() 或者 send() 函数时，不能使用带参数的 send() 函数。

def foo():
    bar_a = yield "hello"
    bar_b = yield bar_a
    yield bar_b

f = foo()
# 当迭代器用
for i in f:
    print(i)
print("***************")
f = foo()
# 当生成器用
print(next(f)) # yield "hello"
print(f.send("world")) # bar_a = "world"; yield bar_a
print(f.send("!")) # bar_b = "!"; yield bar_b

