name = "Python教程"
def demo ():
    #访问全局变量
    print(globals()['name'])
    name = "shell教程"
    print(name)
demo()
print(name)