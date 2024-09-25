class MyClass:
    def __init__(self):
        self.a = 1
        self.b = 2

    def method1(self):
        pass

    def method2(self):
        pass


# 创建一个实例
obj = MyClass()

# 获取对象的属性名称列表
attributes = dir(obj)

# 遍历属性名称，判断是属性还是方法
for attr_name in attributes:
    attr = getattr(obj, attr_name)

    if callable(attr):  # 检查是否为可调用对象（方法）
        print(f"{attr_name} 是方法")
    else:
        print(f"{attr_name} 是属性")





