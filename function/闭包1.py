# 闭包函数 闭合函数
# 在Python中，闭包（Closure）是指一个函数与该函数可以访问的父级函数的变量环境组合而成的一个整体。
# 闭包让你可以在一个外层函数中定义一个内层函数，并且在内层函数中使用外层函数的局部变量，
# 即使外层函数已经返回完毕之后，这些变量仍然可以被访问。

def outer_function(text):
    message = text
    message_2 = text

    def inner_function():
        print(message)

    return inner_function

# 创建闭包
hi_func = outer_function('Hi, I am a message!')
hello_func = outer_function('Hello, another message!')

# 调用闭包中的函数
hi_func()  # 输出: Hi, I am a message!
hello_func()  # 输出: Hello, another message!


# 闭包能够记住并访问定义它的函数的作用域中的变量，即使外部函数已经执行完毕，
# 这使得闭包在处理状态保持和抽象封装方面非常有用。