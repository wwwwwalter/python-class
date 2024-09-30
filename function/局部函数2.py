def outdef():
    name="全局函数中的变量"
    print(name)
    def inner():
        nonlocal name # 非全局变量
        name="局部函数中的变量"
        print(name)
    inner()


outdef()