# 如果被修饰的函数本身带有参数，那应该如何传值呢
def funA(fn):
    # 定义一个嵌套函数
    def say(arc):
        print("Python教程:", arc)

    print("hello")

    return say


# 相当于执行了 funB = funA(funB)
# 给funB赋予了一个新的函数地址say(arc)
# 相当于用旧的函数构造了一个新的函数
@funA
def funB(arc):
    print("funB():", arc)


funB("http://c.biancheng.net/python")
