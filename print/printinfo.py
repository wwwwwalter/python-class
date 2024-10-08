# 1、直接拼接：适用于简单的字符串拼接。
# 2、% 格式化：适用于需要更多控制的情况。
# 3、str.format()：提供了更多的灵活性和控制。
# 4、f-string：简洁且性能较好，推荐用于现代 Python 编程

name = "Alice"
age = 25

# 直接拼接字符串
print("Name:", name, "Age:", age)

# 使用%格式化
print("Name: %s Age: %d" % (name, age))

# 使用str.format()
print("Name: {} Age: {}".format(name, age))
print("Name: {0} Age: {1}".format(name, age))
print("Name: {name} Age: {age}".format(name=name, age=age))

# 使用f-string
print(f"Name: {name} Age: {age}")
