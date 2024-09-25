# 列表（list）、元组（tuple）、字典（dict）、集合（set）这些序列式容器，有个别名：迭代器
# 迭代器指的就是支持迭代的容器，更确切的说，是支持迭代的容器类对象

# 类中必须实现如下 2 个方法：
# __next__(self)：返回容器的下一个元素。
# __iter__(self)：该方法返回一个迭代器（iterator）。


class listDemo:
    def __init__(self):
        print("init")
        self.__data = []
        self.__step = 0

    def __setitem__(self, key, value):
        print("setitem")
        self.__data.insert(key, value)
        self.__step += 1

    # 返回迭代器,每个for循环只在开始时调用一次
    def __iter__(self):
        print("iter")
        return self

    def __next__(self):
        print("next")
        if self.__step <= 0:
            raise StopIteration # 告诉for循环，没有更多元素了
        self.__step -= 1
        return self.__data[self.__step]


mylist = listDemo()
mylist[0] = 1
mylist[1] = 2

for i in mylist:
    print(i)
