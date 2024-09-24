class CLanguage:
    a = 1
    b = 2
    def __init__ (self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"





#通过类名调用__dict__
dics = CLanguage.__dict__

for key,value in dics.items():
    print(key,":",value)


print("-------")
#通过类实例对象调用 __dict__
clangs = CLanguage()
dics1 = clangs.__dict__
for key,value in dics1.items():
    print(key,":",value)




