# 实现 Python 函数返回多个值，有以下 2 种方式：
# 在函数中，提前将要返回的多个值存储到一个列表或元组中，然后函数返回该列表或元组；
# 函数直接返回多个值，之间用逗号（ , ）分隔，Python 会自动将多个值封装到一个元组中，其返回值仍是一个元组。

def return_list():
    add = ["1", "2", "3"]
    return add


def return_tuple():
    return "1", "2", "3"


print(return_list())
print(return_tuple())

pythonadd, shelladd, golangadd = return_list()
print(pythonadd)
print(shelladd)
print(golangadd)

pythonadd, shelladd, golangadd = return_tuple()
print(pythonadd)
print(shelladd)
print(golangadd)
