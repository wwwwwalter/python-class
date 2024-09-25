# 在使用迭代器时，必须将所有数据都存在容器中，否则无法使用迭代器
# 生成器不需要存储数据，只需要计算数据，所以生成器比迭代器更高效

# 函数（生成器函数）
def intNum():
    print("begin")
    for i in range(5):
        yield i
        # return i
        print("yield")


num = intNum() # 调用函数，创建一个生成器,此时不执行”print("begin")“
# 调用生成器函数，Python 解释器也不会执行函数中的代码，它只会返回一个生成器（对象）

# 想使执行完 yield 语句立即暂停的程序得以继续执行，有以下 3 种方式：
# 1.通过生成器（上面程序中的 num）调用 next() 内置函数或者 __next__() 方法；
# 2.通过 for 循环遍历生成器。
# 3.直接将生成器能生成的所有值存储到列表或者元组中

print("***********next************")
next(num) # 第一次执行函数体，到yield语句，暂停
next(num) # 接着执行函数体
num.__next__() # 接着执行函数体
print("***********for************")

# 接着执行函数体
for i in num:
    pass
print("***********list***********")

num = intNum()
list(num)
print("***********tuple***********")

num = intNum()
tuple(num)

