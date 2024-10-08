# map(function, iterable)

listDemo = [1,2,3,4,5]
new_list = map(lambda x:x+1,listDemo)
print(list(new_list))


listDemo1 = [1, 2, 3, 4, 5]
listDemo2 = [3, 4, 5, 6, 7]
new_list = map(lambda x,y: x + y, listDemo1,listDemo2)
print(list(new_list))

# filter(function, iterable)
listDemo = [1, 2, 3, 4, 5]
new_list = filter(lambda x: x % 2 == 0, listDemo)
print(list(new_list))

# reduce(function, iterable)
# function 规定必须是一个包含 2 个参数的函数；iterable 表示可迭代对象。
# 由于 reduce() 函数在 Python 3.x 中已经被移除，放入了 functools 模块
import functools

listDemo = [1, 2, 3, 4, 5]
product = functools.reduce(lambda x, y: x * y, listDemo)
print(product)