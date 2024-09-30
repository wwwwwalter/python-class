# 闭包函数，其中 exponent 称为自由变量
def nth_power(exponent):
    str1="hello"
    str2="world"
    def exponent_of(base):
        print(str1)
        return base ** exponent

    return exponent_of  # 返回值是 exponent_of 函数


square = nth_power(2)  # 计算一个数的平方
cube = nth_power(3)  # 计算一个数的立方
print(square(2))  # 计算 2 的平方
print(cube(2))  # 计算 2 的立方

print(type(square.__closure__)) # tuple
print(square.__closure__) # 所有在内函数中使用到的变量都收录在这个tuple里
