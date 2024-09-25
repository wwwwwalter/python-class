import inspect

class CLanguage:
    pass

# 创建一个实例
clangs = CLanguage()

# 获取所有成员：父类+子类
all_members = dir(clangs)

# 获取继承"类链"：[子类名,父类名]
mro = inspect.getmro(CLanguage)

# 区分继承成员和自定义成员名称
inherited_members = set()   # 名称
custom_members = set()      # 名称



# 遍历继承链中的所有父类
for base_class in mro[1:]:
    print(base_class)
    inherited_members.update(dir(base_class))

# 计算自定义成员
custom_members = set(all_members) - inherited_members

# 打印所有成员
print("所有成员:")
for index, member_name in enumerate(all_members, start=1):
    attr = getattr(clangs, member_name) # 获取属性(内存对象，不是名字字符串)
    if hasattr(attr, "__call__"):   # if callable(attr):
        print(f"{index:02d} (M) {member_name}")
    else:
        print(f"{index:02d} (A) {member_name}")

# 打印继承成员
print("\n继承成员:")
for index, member_name in enumerate(inherited_members, start=1):
    attr = getattr(clangs, member_name)  # 获取属性(内存对象，不是名字字符串)
    if hasattr(attr, "__call__"):   # if callable(attr):
        print(f"{index:02d} (M) {member_name}")
    else:
        print(f"{index:02d} (A) {member_name}")

# 打印自定义成员
print("\n自定义成员:")
for index, member_name in enumerate(custom_members, start=1):
    attr = getattr(clangs, member_name)  # 获取属性(内存对象，不是名字字符串)
    if hasattr(attr, "__call__"):   # if callable(attr):
        print(f"{index:02d} (M) {member_name}")
    else:
        print(f"{index:02d} (A) {member_name}")
