# 创建一个全局变量字典
globals_dict = {'x': 10, 'y': 20}

# 使用 exec 在提供的全局作用域中执行代码
code = 'z = x + y'
exec(code, globals_dict)

# 访问变量 z
print(globals_dict['z'])  # 输出: 30