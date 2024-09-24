import inspect

class CLanguage:
    pass

clangs = CLanguage()

# 获取所有成员
all_members = dir(clangs)

# 获取继承链
mro = inspect.getmro(CLanguage)

# 区分继承成员和自定义成员
inherited_members = set()
custom_members = set()



# 遍历继承链中的类
for base_class in mro[1:]:
    inherited_members.update(dir(base_class))

# 计算自定义成员
custom_members = set(all_members) - inherited_members

# 打印所有成员
print("所有成员:")
for index, func in enumerate(all_members, start=1):
    print(index, func)

# 打印继承成员
print("\n继承成员:")
for index, func in enumerate(inherited_members, start=1):
    print(index, func)

# 打印自定义成员
print("\n自定义成员:")
for index, func in enumerate(custom_members, start=1):
    print(index, func)
