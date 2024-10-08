# 方式一：使用列表推导式
my_list = [1, 2, 3, 4, 5, 3]
value_to_remove = 3

my_list = [x for x in my_list if x != value_to_remove]

print(my_list)  # 输出: [1, 2, 4, 5]


# 方式二：使用 remove() 方法
my_list = [1, 2, 3, 4, 5, 3]

try:
    my_list.remove(3)  # 删除第一个出现的值为3的元素
except ValueError:
    print("要删除的值不在列表中")

print(my_list)  # 输出: [1, 2, 4, 5, 3]


# 方式三：使用索引遍历并删除
my_list = [1, 2, 3, 4, 5, 3]
value_to_remove = 3
# range(len(my_list) - 1, -1, -1)：从列表的最后一个索引开始，向前遍历到第一个索引。
# 这样做是为了避免在删除元素后影响后续元素的索引。
for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] == value_to_remove:
        del my_list[i]

print(my_list)  # 输出: [1, 2, 4, 5]


# 方式四：使用 while 循环
# 另一种方法是使用 while 循环，这种方法也避免了在遍历过程中直接修改列表的问题。
my_list = [1, 2, 3, 4, 5, 3]
value_to_remove = 3

i = 0
while i < len(my_list):
    if my_list[i] == value_to_remove:
        del my_list[i]
    else:
        i += 1

print(my_list)  # 输出: [1, 2, 4, 5]