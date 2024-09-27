import inspect


def get_all_members(cls, show_method=True, show_attribute=True):
    """
    获取一个类的所有成员，包括继承的成员和自定义的成员
    :param cls: 类对象
    :param show_method: 是否显示方法
    :param show_attribute: 是否显示属性
    :return:
    """

    # 获取所有成员：父类+子类
    all_members = dir(cls)

    # 获取继承"类链"：[子类名,父类名]
    mro = inspect.getmro(cls)

    # 区分继承成员和自定义成员名称
    inherited_members = set()   # 名称
    custom_members = set()      # 名称


    # 遍历输出继承链
    print("继承链条")
    for base_class in mro:
        print(base_class.__name__)


    # 遍历继承链中的所有父类
    for base_class in mro[1:]:
        inherited_members.update(dir(base_class))

    # 计算自定义成员
    custom_members = set(all_members) - inherited_members

    # 打印所有成员
    print("所有成员:")
    for index, member_name in enumerate(all_members, start=1):
        attr = getattr(cls, member_name) # 获取属性(内存对象，不是名字字符串)
        if hasattr(attr, "__call__"):   # if callable(attr):
            print(f"{index:02d} (M) {member_name}") if show_method else None
        else:
            print(f"{index:02d} (A) {member_name}") if show_attribute else None

    # 打印继承成员
    print("\n继承成员:")
    for index, member_name in enumerate(inherited_members, start=1):
        attr = getattr(cls, member_name)  # 获取属性(内存对象，不是名字字符串)
        if hasattr(attr, "__call__"):   # if callable(attr):
            print(f"{index:02d} (M) {member_name}") if show_method else None
        else:
            print(f"{index:02d} (A) {member_name}") if show_attribute else None

    # 打印自定义成员
    print("\n自定义成员:")
    for index, member_name in enumerate(custom_members, start=1):
        attr = getattr(cls, member_name)  # 获取属性(内存对象，不是名字字符串)
        if hasattr(attr, "__call__"):   # if callable(attr):
            print(f"{index:02d} (M) {member_name}") if show_method else None
        else:
            print(f"{index:02d} (A) {member_name}") if show_attribute else None


# 本文件测试用
if __name__ == '__main__':
    d = {"name": "John", "age": 30}

    get_all_members(type(d),True,True)