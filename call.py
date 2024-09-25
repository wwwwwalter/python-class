class CLanguage:
    def __call__(self, *args, **kwargs):
        print("CLanguage call")

clangs = CLanguage()
clangs("C语言中文网")

# 可调用对象：通过在 CLanguage 类中实现 __call__() 方法，使的 clangs 实例对象变为了可调用对象。

clangs.__call__("C语言中文网")