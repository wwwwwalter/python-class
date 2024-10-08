import copy

list1 = [[1, 2], (30, 40)]
# list2 = list1.copy() # 浅拷贝
list2 = copy.deepcopy(list1) # 深拷贝



print(id(list1))
print(id(list2))
print("----")

print(id(list1[0])) # 不同
print(id(list2[0]))
print("----")

print(id(list1[1])) # 相同
print(id(list2[1]))
# deepcopy 对于不可变对象（如元组）不会创建新的对象，而是直接引用原来的对象。
# 当你修改 list1[1] 时，实际上创建了一个新的元组，并将它赋值给 list1[1]，
# 因此 list1[1] 的 ID 发生了变化，而 list2[1] 的 ID 保持不变。
print("----")

list1[1] += (50, 60)
print("list1:", list1)
print("list2:", list2)

print(id(list1[1]))
print(id(list2[1]))
