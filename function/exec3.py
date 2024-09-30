# 创建全局变量字典
globals_dict = {'x': 10, 'y': 20}

# 创建局部变量字典
locals_dict = {'x': 5}  # 局部作用域中的 x 值覆盖全局作用域中的 x

# 使用 exec 在提供的全局和局部作用域中执行代码
code = 'z = x + y'
exec(code, globals_dict, locals_dict)

# 访问变量 z
print(locals_dict['z'])  # 输出: 25