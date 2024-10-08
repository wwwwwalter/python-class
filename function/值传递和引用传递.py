# Python 中，根据实际参数的类型不同，函数参数的传递方式可分为 2 种，分别为值传递和引用（地址）传递：
# 值传递：适用于实参类型为不可变类型（字符串、数字、元组）； string int tuple
# 引用（地址）传递：适用于实参类型为可变类型（列表，字典，集合）；list dict set

# 在 Python 中，对于可变类型（如列表、字典、集合等）使用引用传递的原因主要有以下几点：
# 内存效率：
# 可变对象通常较大或复杂，直接复制整个对象会消耗大量内存。
# 引用传递可以避免不必要的内存开销，提高程序运行效率。
# 性能考虑：
# 如果每次函数调用都复制整个对象，会导致性能下降，尤其是在处理大数据量时。
# 引用传递只需要传递对象的内存地址，操作更加高效。
# 一致性：
# Python 设计的一致性原则要求不同类型的数据有不同的处理方式。不可变类型（如数字、字符串、元组）因为其不可变性，复制不会引起副作用；而可变类型则可能需要在函数内部进行修改。
# 设计灵活性：
# 引用传递使得函数可以在原地修改数据，增加了编程的灵活性。
# 这种机制允许函数内部的操作直接作用于外部数据，减少了返回值的复杂度。


def demo(obj) :
    obj += obj
    print("形参值为：",obj)
print("-------值传递-----")
a = "C语言中文网"
print("a的值为：",a)
demo(a)
print("实参值为：",a)
print("-----引用传递-----")
a = [1,2,3]
print("a的值为：",a)
demo(a)
print("实参值为：",a)


# -------值传递-----
# a的值为： C语言中文网
# 形参值为： C语言中文网C语言中文网
# 实参值为： C语言中文网
# -----引用传递-----
# a的值为： [1, 2, 3]
# 形参值为： [1, 2, 3, 1, 2, 3]
# 实参值为： [1, 2, 3, 1, 2, 3]