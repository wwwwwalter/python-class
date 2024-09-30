def text():
    global add  # 不能赋值
    add = "http"
    print("函数体内访问:", add)


text()
print("函数体外访问:", add)

gs = globals()
for key,value in gs.items():
    print(key,value)