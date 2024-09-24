class MyClass:
    a = 1  # 类属性
    b = 2  # 类属性

    def __init__(self):
        self.name = "MyClass"  # 实例属性
        self.url = "http://example.com"  # 实例属性

    def my_method(self):  # 方法
        print("This is a method")

    @property
    def my_property(self):  # 属性
        return "This is a property"

# 模块级别的函数
def my_function():
    print("This is a module-level function")

# 模块级别的变量
my_variable = 10
