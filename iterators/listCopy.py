# 浅拷贝
original_list = [1, 2, 3, 4, 5]

# 使用 copy() 方法创建一个浅拷贝
# 对于只包含基本数据类型的列表（如整数、字符串等），
# 浅拷贝和深拷贝的效果是一样的，即新列表会包含一份原始列表中所有元素的副本。
copied_list = original_list.copy()

print("Original list:", original_list)  # 输出: Original list: [1, 2, 3, 4, 5]
print("Copied list:", copied_list)      # 输出: Copied list: [1, 2, 3, 4, 5]

# 修改原列表
original_list.append(6)

print("After modifying original list:")
print("Original list:", original_list)  # 输出: Original list: [1, 2, 3, 4, 5, 6]
print("Copied list:", copied_list)      # 输出: Copied list: [1, 2, 3, 4, 5]
# 对于只包含基本数据类型的列表（如整数、字符串等），
# 浅拷贝和深拷贝的效果是一样的，即新列表会包含一份原始列表中所有元素的副本。