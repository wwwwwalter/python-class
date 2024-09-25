# attr.__code__ 是用来访问一个函数或方法的代码对象（code object）。在 Python 中，每一个函数都有一个 __code__ 属性，这个属性返回一个 code object，它包含了函数的字节码和其他相关信息。

def example_function(a, b):
    return a + b

# 访问函数的 __code__ 属性
code_obj = example_function.__code__

# 打印 code object 的信息
print(f"Code object: {code_obj}")

# 获取 code object 的各种属性
print(f"Co_argcount: {code_obj.co_argcount}")  # 参数数量
print(f"Co_posonlyargcount: {code_obj.co_posonlyargcount}")  # 仅位置参数的数量
print(f"Co_kwonlyargcount: {code_obj.co_kwonlyargcount}")  # 仅关键字参数的数量
print(f"Co_nlocals: {code_obj.co_nlocals}")  # 局部变量的数量
print(f"Co_stacksize: {code_obj.co_stacksize}")  # 栈大小
print(f"Co_flags: {code_obj.co_flags}")  # 标志位
print(f"Co_code: {code_obj.co_code}")  # 字节码
print(f"Co_consts: {code_obj.co_consts}")  # 常量
print(f"Co_names: {code_obj.co_names}")  # 名称
print(f"Co_varnames: {code_obj.co_varnames}")  # 变量名称
print(f"Co_filename: {code_obj.co_filename}")  # 文件名
print(f"Co_name: {code_obj.co_name}")  # 函数名
print(f"Co_firstlineno: {code_obj.co_firstlineno}")  # 第一行号
print(f"Co_lnotab: {code_obj.co_lnotab}")  # 行号表
print(f"Co_freevars: {code_obj.co_freevars}")  # 闭包变量
print(f"Co_cellvars: {code_obj.co_cellvars}")  # 单元格变量
