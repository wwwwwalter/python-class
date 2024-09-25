def funA(fn):
    print("C语言中文网")
    fn()  # 执行传入的fn参数
    print("http://c.biancheng.net")
    return "返回一个字符串类型"


# 使用 @funA 时，funA 会在定义 funB 时立即执行，并返回一个新的函数。
# 相当于 funB = funA(funB)
@funA
def funB():
    print("学习 Python")
    
# 被“＠函数”修饰的函数不再是原来的函数，
# 而是被替换成一个新的东西（取决于装饰器的返回值）
# 此时funB已经变成string类型了,和装饰器的return类型有关
print(type(funB)) # string

