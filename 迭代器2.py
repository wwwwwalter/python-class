class listDemo:
    def __init__(self):
        self.__date=[]
        self.__step=0

    def __setitem__(self, key, value):
        self.__date.insert(key,value)
        self.__step+=1

    def __call__(self):
        self.__step-=1
        return self.__date[self.__step]

mylist=listDemo()
mylist[0]=1
mylist[1]=2
mylist[2]=3

a = iter(mylist,1)

for i in a:
    print(i)

# 这里介绍 iter() 函数第 2 个参数的作用，
# 如果使用该参数，则要求第一个 obj 参数必须传入可调用对象（可以不支持迭代），
# 这样当使用返回的迭代器调用 __next__() 方法时，它会通过执行 obj() 调用 __call__() 方法，
# 如果该方法的返回值和第 2 个参数值相同，则输出 StopInteration 异常；
# 反之，则输出 __call__() 方法的返回值。



