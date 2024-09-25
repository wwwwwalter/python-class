def funA(fn):
    def say(*args,**kwargs):
        print(args)
        print(kwargs)
    return say


@funA
def funB(arc):
    pass


@funA
def other_funB(name,arc):
    pass

@funA
def multiple_funB(*args,**kwargs):
    pass

funB("http://c.biancheng.net")
other_funB("百度","http://www.baidu.com")
multiple_funB(1,2,3,4,5,6,web="C语言中文网",url="http://c.biancheng.net")