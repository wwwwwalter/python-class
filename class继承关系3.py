class CLanguage:
    a = 1
    b = 2

    def __init__(self):
        self.name = "C"
        self.add = "http"


class CL(CLanguage):
    c = 1
    d = 2

    def __init__(self):
        super().__init__()
        self.version = "1.0"
        self.url = "https://example.com"


# 查看父类的 __dict__
father_dict = CLanguage.__dict__
print("父类的 __dict__:")
for key, value in father_dict.items():
    print(f"father class  {key} {value}")

# 查看子类的 __dict__
son_dict = CL.__dict__
print("\n子类的 __dict__:")
for key, value in son_dict.items():
    print(f"son class  {key} {value}")

# 创建一个父类实例
father_instance = CLanguage()
print("\n父类实例的 __dict__:")
for key, value in father_instance.__dict__.items():
    print(f"father instance  {key} {value}")

# 创建一个子类实例
instance = CL()

# 查看子类实例的 __dict__
instance_dict = instance.__dict__
print("\n子类实例的 __dict__:")
for key, value in instance_dict.items():
    print(f"instance  {key} {value}")
