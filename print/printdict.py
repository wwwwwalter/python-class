# 字符串模板中使用key

# 使用 % 格式化
formats = '教程是：%(name)s, 价格是：%(price).2f, 网址是：%(url)s'
data = {'name': 'Python教程', 'price': 9.9, 'url': 'http://c.biancheng.net/python/'}
print(formats % data)

# 使用 str-format 格式化
formats = '教程是：{name}, 价格是：{price:.2f}, 网址是：{url}'
data = {'name': 'Python教程', 'price': 9.9, 'url': 'http://c.biancheng.net/python/'}
print(formats.format(**data))

# 使用 f-string 格式化
data = {'name': 'Python教程', 'price': 9.9, 'url': 'http://c.biancheng.net/python/'}
print(f'教程是：{data["name"]}, 价格是：{data["price"]:.2f}, 网址是：{data["url"]}')
