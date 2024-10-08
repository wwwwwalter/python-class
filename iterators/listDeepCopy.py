import copy

original_list = [1, 2, [3, 4], 5]

# 使用 deepcopy 方法创建一个深拷贝
deep_copied_list = copy.deepcopy(original_list)
# deep_copied_list = original_list.copy() # 如果使用浅拷贝，最后的输出就会有6

print("Original list:", original_list)  # 输出: Original list: [1, 2, [3, 4], 5]
print("Deep copied list:", deep_copied_list)  # 输出: Deep copied list: [1, 2, [3, 4], 5]

# 修改原列表中的嵌套列表
original_list[2].append(6)

print("After modifying nested list in original list:")
print("Original list:", original_list)  # 输出: Original list: [1, 2, [3, 4, 6], 5]
print("Deep copied list:", deep_copied_list)  # 输出: Deep copied list: [1, 2, [3, 4], 5]